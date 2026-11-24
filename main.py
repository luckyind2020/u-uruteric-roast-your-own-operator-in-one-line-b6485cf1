"""Roast Your Own Operator in One Line — entry runner.

Reads the single roast line from entry.txt and prints it.
"""

from pathlib import Path


def load_roast() -> str:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")
    line = text.strip()
    if not line:
        raise SystemExit("entry.txt is empty — nothing to roast with")
    if "\n" in line:
        raise SystemExit("entry must be exactly one line")
    return line


def main() -> None:
    print(load_roast())


if __name__ == "__main__":
    main()
