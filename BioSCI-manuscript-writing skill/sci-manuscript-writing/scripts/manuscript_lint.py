#!/usr/bin/env python3
"""Read-only, dependency-free surface check for SCI manuscript text or .docx.

Usage:
    python scripts/manuscript_lint.py /path/to/draft.docx

This is a heuristic language scan; it does not verify scientific claims, data,
statistical appropriateness, original figures, or citation-source relevance.
"""

import argparse
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile, BadZipFile

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def get_text(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {'.txt', '.md'}:
        return path.read_text(encoding='utf-8-sig')
    if ext != '.docx':
        raise ValueError('Supported file types: .docx, .txt, .md')
    try:
        with ZipFile(path, 'r') as archive:
            root = ET.fromstring(archive.read('word/document.xml'))
    except (BadZipFile, KeyError, ET.ParseError) as exc:
        raise ValueError(f'Invalid or unreadable DOCX: {exc}') from exc
    parts = []
    for paragraph in root.iter(W + 'p'):
        text = ''.join(node.text or '' for node in paragraph.iter(W + 't'))
        if text.strip():
            parts.append(text)
    return '\n'.join(parts)


PATTERNS = [
    ('duplicate-word', re.compile(r'\b([A-Za-z]{3,})\s+\1\b', re.I),
     'Repeated word: check whether it was duplicated.'),
    ('contradictory-transition', re.compile(r'\b(?:First|Second|Third),\s*(?:Nevertheless|However|Although)\b', re.I),
     'Transition is likely redundant or ungrammatical.'),
    ('maybe-as-modal', re.compile(r'\bmaybe\s+(?:alter|change|reduce|increase|affect|contribute|promote|impair|mediate)\b', re.I),
     'Consider modal "may" rather than adverb "maybe".'),
    ('unit-spacing', re.compile(r'\b\d+(?:\.\d+)?\s*°C\b'),
     'Check temperature formatting: use "37 °C".'),
    ('sample-size-spacing', re.compile(r'\bn\s*=\s*\d+\b'),
     'Check sample-size formatting: use "n = 3".'),
    ('unnamed-hospital', re.compile(r'\b(?:from|at) hospital\b', re.I),
     'Name the hospital or revise the phrasing.'),
    ('reader-article', re.compile(r'\busing\s+(?:SpectraMax|BioTek|TECAN)\s+\S+\s+(?:microplate\s+)?reader\b', re.I),
     'Consider an article before instrument name ("using a ... reader").'),
]


def lint(text: str):
    output = []
    for no, line in enumerate(text.splitlines(), start=1):
        for rule, pat, advice in PATTERNS:
            for match in pat.finditer(line):
                token = match.group(0)
                # Filter already-correct whitespace variants that match broad patterns.
                if rule == 'unit-spacing' and re.search(r'\s°', token):
                    continue
                if rule == 'sample-size-spacing' and re.fullmatch(r'n = \d+', token):
                    continue
                output.append((no, rule, token, advice))
    if re.search(r'\bgray\b', text, re.I) and re.search(r'\bgrey\b', text, re.I):
        output.append((0, 'colour-consistency', 'gray / grey', 'Select one spelling consistently.'))
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path, help='Input DOCX, Markdown or text file')
    args = parser.parse_args()
    try:
        text = get_text(args.file)
        problems = lint(text)
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    print(f'File: {args.file.name}')
    print(f'Potential surface issues: {len(problems)}')
    for line_no, rule, match, advice in problems:
        position = f'paragraph/line {line_no}' if line_no else 'document-wide'
        print(f'- [{rule}] {position}: {match!r} — {advice}')
    print('NOTE: Heuristic only. Check all scientific claims, methods, figures, and sources manually.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
