"""Menu for opening the calculators in this folder."""

from pathlib import Path
import subprocess
import sys


CALCULATORS = {
    "1": ("Arithmetic Progression", "arithmatic progression.py"),
    "2": ("Co-ordinate Geometry", "co-ordinategeomerty.py"),
    "3": ("Financial Planning", "financial planning.py"),
}


def main():
    folder = Path(__file__).resolve().parent

    while True:
        print("\nChoose a calculator to open:")
        for number, (name, _) in CALCULATORS.items():
            print(f"{number}. {name}")
        print("q. Quit")

        choice = input("Enter your choice: ").strip().lower()
        if choice == "q":
            print("Goodbye!")
            break

        calculator = CALCULATORS.get(choice)
        if calculator is None:
            print("Invalid choice. Please try again.")
            continue

        name, filename = calculator
        path = folder / filename
        if not path.is_file():
            print(f"Could not find {filename}.")
            continue

        print(f"\nOpening {name}...\n")
        subprocess.run([sys.executable, str(path)], check=False)


if __name__ == "__main__":
    main()
