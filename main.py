#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line -- the funniest excuse a robot vacuum gives for missing
a spot -- to /output/entry.txt.

Python 3.13 standard library only. No network, no input files, no
arguments: the excuse is fixed in this file, so every run writes the
exact same bytes.

The joke: the vacuum's own sensors misfire. Its object classifier
decides a crumb is a small pet, so it spares it -- and the deadpan
kicker is the vacuum drawing a moral line about eating pets, as if
suction were a choice. First-person machine voice, rooted in the
vacuum's own world (sensors, classification), with the turn landing
on the last four words.
"""

import os
from pathlib import Path

EXCUSE = (
    "My sensors classified that crumb as a small pet, "
    "so I left it alone. I don't eat pets."
)


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # 1-140 characters, one line, not only whitespace.
    if not 1 <= len(EXCUSE) <= 140:
        raise ValueError(f"excuse is {len(EXCUSE)} characters, must be 1-140")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be a single line")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(EXCUSE, encoding="utf-8")
    # Read it back and confirm the bytes on disk are exactly the excuse:
    # a silent truncation or encoding change must fail loudly, not ship.
    if entry.read_text(encoding="utf-8") != EXCUSE:
        raise ValueError("entry.txt on disk does not match the excuse")
    print(f"Wrote {len(EXCUSE)} characters to {entry}")


if __name__ == "__main__":
    main()
