#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""NapTrack Pro pitches the worst app idea ever, in one sentence.

This program exists for the make.fun bounty "The Worst App Idea Ever
Pitched". Running it drops a single 158-character sentence into
/output/entry.txt. The run is fully deterministic: no randomness, no
clock reads, no network calls and no user input, so repeated runs
produce byte-identical files.
"""

from pathlib import Path

PITCH = (
    "Introducing NapTrack Pro: an app that tracks exactly how "
    "long your phone naps while you sleep, then charges you "
    "$4.99 a month to remind you it was asleep too."
)

DESTINATION = Path("/output/entry.txt")


def run() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    run()
