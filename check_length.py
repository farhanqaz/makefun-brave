from pathlib import Path

ENTRY_FILE = Path("/output/entry.txt")
MAX_LENGTH = 280


def main() -> None:
    text = ENTRY_FILE.read_text(encoding="utf-8")
    length = len(text)
    valid = 1 <= length <= MAX_LENGTH and bool(text.strip())
    print(f"Code points: {length}")
    print(f"Valid: {'yes' if valid else 'no'}")


if __name__ == "__main__":
    main()
