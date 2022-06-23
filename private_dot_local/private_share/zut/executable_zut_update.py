#! /bin/env python3
import json
import pathlib
import os

ZUT_DIRECTORY = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))


def update_vscode():
    print(" - VSCode...")
    with open(
        pathlib.Path("~/.config/Code/User/keybindings.json").expanduser(), "r"
    ) as f:
        shortcuts = json.loads("\n".join(f.readlines()[1:]))
    with open(ZUT_DIRECTORY / "vscode.txt", "w") as f:
        f.writelines(
            [f"{shortcut['key']} => {shortcut['command']}\n" for shortcut in shortcuts]
        )


def main():
    print("Updating zut cheatsheets...")
    update_vscode()
    print("Cheatsheets up to date !")
    print("Use alias 'zut' or press Ctrl-H from terminal to search cheatsheets")


if __name__ == "__main__":
    main()
