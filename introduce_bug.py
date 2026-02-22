"""Demo: Introduce a bug for the Auto-Heal demo.

Run this script to create a commit that breaks the add() function:
    python introduce_bug.py

This is for local/demo use only — it modifies src/math_utils.py in place.
"""

from pathlib import Path


def main():
    target = Path(__file__).parent / "src" / "math_utils.py"
    content = target.read_text()

    if "return a - b  # BUG" in content:
        print("Bug already introduced. Reverting...")
        content = content.replace("return a - b  # BUG", "return a + b")
        target.write_text(content)
        print("Reverted: add() now returns a + b")
    else:
        content = content.replace(
            "    return a + b",
            "    return a - b  # BUG",
            1,
        )
        target.write_text(content)
        print("Bug introduced: add() now returns a - b")
        print("Commit and push to trigger CI failure.")


if __name__ == "__main__":
    main()
