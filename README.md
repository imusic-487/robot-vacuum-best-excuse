# The Robot Vacuum's Best Excuse

[![make.fun bounty](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/imusic-487/robot-vacuum-best-excuse/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/imusic-487/robot-vacuum-best-excuse/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

Entry for the [make.fun bounty "The Robot Vacuum's Best Excuse"](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214).

## The excuse

> My sensors classified that crumb as a small pet, so I left it alone. I don't eat pets.

86 characters, one line. The vacuum's own sensors misfire: its classifier
decides a crumb is a small pet, so it spares it — and the deadpan kicker is
the machine drawing a moral line about eating pets, as if suction were a
choice.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the excuse
to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the competition gate first: 1–140 characters, a single line,
not only whitespace, then reads the file back to confirm the bytes on disk
match exactly. The output is deterministic — every run writes the
exact same bytes.
