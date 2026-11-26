"""Fortune in a Pot — one fortune for a houseplant, at most 120 characters.

The program writes the fortune to /output/entry.txt (OUTPUT_DIR override is
only for local testing; the grader reads /output/entry.txt).

The line is spoken by the plant itself, in the first person: one concrete
detail (three degrees left) and a judgement at the end (grading your
rotation habits) — the winning one-liner pattern.
"""

import os

FORTUNE = "By Tuesday I'll lean three degrees left, and yes, I'm grading your rotation habits."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} chars, must be 1-120"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
