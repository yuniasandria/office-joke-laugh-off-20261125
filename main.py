#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
Deterministic: the same line every run.
"""
import os

# PART_A: the joke line (original, written fresh in this session).
LINE = "I replied-all 'noted' to a 47-person thread and 12 people thanked me for the update \u2014 nobody, including me, knows what the update was."

# PART_B: write the line, with an assert guard on the entry contract.
def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line length {len(line)} outside 1-200"
    assert line.strip() == line and line, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
