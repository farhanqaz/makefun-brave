"""Writes the entry text for make.fun's 'Make the AI judge feel brave' bounty to /output/entry.txt, deterministically.

Run with --stdout to print the text instead of writing the file.
"""
import argparse
from pathlib import Path

TEXT = """The tent was smaller than the dark around it.
Something moved out past the trees and stopped.
I lay still and listened until listening
was the same as sleeping.
In the morning there were deer tracks by the flap,
ordinary as a sentence, and I made tea."""

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MAX_LENGTH = 280


def validate(text: str) -> None:
    length = len(text)
    if length < 1 or length > MAX_LENGTH:
        raise SystemExit(f"TEXT must be 1-{MAX_LENGTH} code points, got {length}")
    if not text.strip():
        raise SystemExit("TEXT must not be only whitespace")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write the bounty entry text.")
    parser.add_argument("--stdout", action="store_true", help="print the text and do not write the file")
    args = parser.parse_args(argv)
    validate(TEXT)
    if args.stdout:
        print(TEXT)
        return
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(TEXT, encoding="utf-8", newline="")
    print(f"Wrote {len(TEXT)} code points to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
