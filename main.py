"""One Line, One Laugh - variant 2.

Writes a single original funny line to /output/entry.txt.
Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os

LINE = "The hotel left a mint on my pillow and a bill for the mint on the nightstand."


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
