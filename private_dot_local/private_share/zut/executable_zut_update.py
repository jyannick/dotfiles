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


def update_git():
    print(" - git...")
    git_config_output = os.popen("git config --get-regexp alias")
    with open(ZUT_DIRECTORY / "git.txt", "w") as f:
        f.writelines(
            [
                f"git {alias.split()[0].replace('alias.', '')} => git {' '.join(alias.split()[1:])}\n"
                for alias in git_config_output
            ]
        )


def main():
    print("Updating zut cheatsheets...")
    update_vscode()
    update_git()
    print("Cheatsheets up to date !")
    print("Use alias 'zut' or press Ctrl-H from terminal to search cheatsheets")


if __name__ == "__main__":
    main()
