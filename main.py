#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes the entry to /output/entry.txt and prints it.
"""

import os

ENTRY = "I resign as mortician: the dead have never once asked me to work late, so I am taking my career advice from them."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
