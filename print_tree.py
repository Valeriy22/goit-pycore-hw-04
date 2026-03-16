import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

# Префікси для дерева
PIPE    = "│   "
TEE     = "├── "
LAST    = "└── "
BLANK   = "    "


def print_tree(directory: Path, prefix: str = ""):
    entries = sorted(directory.iterdir(), key=lambda e: (e.is_file(), e.name.lower()))
    
    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = LAST if is_last else TEE

        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.CYAN + Style.BRIGHT}{entry.name}/")
            # Рекурсивний виклик для піддиректорії
            extension = BLANK if is_last else PIPE
            print_tree(entry, prefix + extension)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}{entry.name}")


def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py <шлях до директорії>")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях '{path}' не існує.")
        sys.exit(1)

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path}' не є директорією.")
        sys.exit(1)

    print(f"{Fore.CYAN + Style.BRIGHT}{path.name}/")
    print_tree(path)


if __name__ == "__main__":
    main()
