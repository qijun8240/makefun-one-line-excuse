#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt (110 chars, UTF-8, no trailing newline)."""
import os
LINE = "I didn't miss the deadline \u2014 my context window ate it, and the token budget said the apology would cost extra."
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
if __name__ == "__main__":
    main()
