import os
import pathlib
from rich.tree import Tree
from rich.console import Console
from rich.text import Text
from rich.style import Style
from style import rich_theme

console = Console(theme=rich_theme)

def get_subdirectories(dir):
    """Get first level subdirectories of a directory"""
    subdirectories = []

    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)
        if os.path.isdir(item_path):
            subdirectories.append(item)

    return subdirectories

def walk_directory(dir: pathlib.Path, tree: Tree):
    """Walk a directory and add it to a Tree"""
    paths = sorted(pathlib.Path(dir).iterdir())
    
    for path in paths:
        if path.is_dir():
            style = "dim" if path.name.startswith("__") else ""
            branch = tree.add(
                f"[bold magenta]:open_file_folder: {path.name}",
                style = style,
                guide_style = style,
            )
            walk_directory(path, branch)

def clean_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pause(error_msg):
    """Pause the program and show an exception message"""
    console.print(error_msg, style="error")
    console.print("Press any key to continue...", end="", style="continue")

    if os.name == 'nt':
        os.system('pause >nul')
    else:
        os.system("bash -c 'read -r -n 1 -s'")
    
    print()