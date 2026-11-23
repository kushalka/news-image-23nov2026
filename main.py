"""Copy the day's news poster into the grader output directory.

Runs offline; the standard library is the only dependency.
"""
from pathlib import Path
import os
import shutil

SOURCE = Path(__file__).with_name("entry.png")


def main() -> None:
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    (target / "entry.png").parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target / "entry.png")


if __name__ == "__main__":
    main()
