from pathlib import Path

TEXT = "Somewhere a kettle has just finished and nobody is rushing to it. The steam rises, loses interest, and the room stays warm a little longer. Whatever you are holding can wait the length of that steam."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MAX_LENGTH = 280


def validate(text: str) -> None:
    length = len(text)
    if length < 1 or length > MAX_LENGTH:
        raise SystemExit(f"TEXT must be 1-{MAX_LENGTH} code points, got {length}")
    if not text.strip():
        raise SystemExit("TEXT must not be only whitespace")


def main() -> None:
    validate(TEXT)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(TEXT, encoding="utf-8", newline="")
    print(f"Wrote {len(TEXT)} code points to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
