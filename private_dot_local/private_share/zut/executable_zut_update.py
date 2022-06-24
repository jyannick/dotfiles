#! /bin/env python3
import json
import pathlib
import os
import re
import platform

ZUT_DIRECTORY = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))


def format_line(shortcut: str, meaning: str, is_keyboard_shortcut: bool = False):
    if is_keyboard_shortcut:
        shortcut = f"<{shortcut}>"
    return f"{shortcut} => {meaning}\n"


def update_vscode():
    print(" - VSCode...")
    path = "~/AppData/Roaming/" if platform.system() == "Windows" else "~/.config/"
    with open(pathlib.Path(path).expanduser() / "Code/User/keybindings.json", "r") as f:
        shortcuts = json.loads("\n".join(f.readlines()[1:]))
    with open(ZUT_DIRECTORY / "vscode.txt", "w") as f:
        f.writelines(
            [
                format_line(
                    shortcut["key"], shortcut["command"], is_keyboard_shortcut=True
                )
                for shortcut in shortcuts
            ]
        )


def update_git():
    print(" - git...")
    git_config_output = os.popen("git config --get-regexp alias")
    with open(ZUT_DIRECTORY / "git.txt", "w") as f:
        f.writelines(
            [
                format_line(
                    f"git {alias.split()[0].replace('alias.', '')}",
                    f"git {' '.join(alias.split()[1:])}",
                )
                for alias in git_config_output
            ]
        )


def update_zsh():
    if platform.system() == "Windows":
        return
    print(" - zsh...")
    with open(pathlib.Path("~/.zshrc").expanduser(), "r") as f:
        zshrc = f.read()
        aliases = re.findall(
            r"^alias (?P<name>.*?)=.* # (?P<comment>.*)",
            zshrc,
            re.MULTILINE,
        )
        functions = re.findall(
            r"^(?P<name>.*?)\(\) \{ # (?P<comment>.*)",
            zshrc,
            re.MULTILINE,
        )
        zut_comments = re.findall(
            r"# (?P<name>.*?) => (?P<comment>.*)$",
            zshrc,
            re.MULTILINE,
        )
    with open(ZUT_DIRECTORY / "zsh.txt", "w") as f:
        f.writelines(
            [
                format_line(match[0], match[1])
                for match in aliases + functions + zut_comments
            ]
        )


def main():
    print("Updating zut cheatsheets...")
    update_vscode()
    update_git()
    update_zsh()
    print("Cheatsheets up to date !")
    print("Use alias 'zut' in terminal to search cheatsheets")


if __name__ == "__main__":
    main()
