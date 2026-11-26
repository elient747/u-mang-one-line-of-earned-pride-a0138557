#!/usr/bin/env python3
"""One Line of Earned Pride — one original line, 1 to 240 characters, a
quiet, earned moment of pride for someone in a scene.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
# Revised: the line is built inside write_entry(); entry.txt mirrors it
# exactly. (Rev 2: named the nurse "Mara" and kept the payoff in the last
# clause — the baby walks out on his own two feet.)
import os


def write_entry():
    line = (
        "After eleven years of night shifts, Mara watched the premature "
        "baby she had fed drop by drop walk out of the ward on his own "
        "two feet, holding his mother's hand."
    )
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
