#!/usr/bin/env python3
"""NapTrack Pro — the worst app idea ever pitched.

A tiny deterministic program for the make.fun bounty
"The Worst App Idea Ever Pitched". It writes exactly one sentence —
a pitch for an app nobody on earth needs — to /output/entry.txt.

The output is byte-identical on every run: no randomness, no clock,
no network, no input. The sentence is 158 characters, inside the
bounty cap of 240.
"""

import os

ENTRY = (
    "Introducing NapTrack Pro: an app that tracks exactly how long "
    "your phone naps while you sleep, then charges you $4.99 a month "
    "to remind you it was asleep too."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
