#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis -- make.fun entry.

Writes one deadpan clinical diagnosis to <output dir>/entry.txt.
Stdlib only, no network, no reads outside the repo.
"""

import os
from pathlib import Path

# The diagnosis itself, typed here by hand: a calm clinical verdict on a
# very human habit, with the laugh landing on the last few words.
ENTRY = (
    "Diagnosis: chronic doomscrolling \u2014 your thumb has developed "
    "separation anxiety and checks the feed just to make sure it "
    "still exists."
)


def main() -> None:
    # Gate check, same as the house gate: 1-200 chars, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
