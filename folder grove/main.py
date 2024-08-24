from functions.subfolder import new_preset, subfolder, show_presets, saved_presets, load, get_subdirectories, walk_directory, FORBIDDEN
from style import custom_style_fancy, rich_theme, style_tree
from rich.console import Console
from json import load as jsload
import os
import shutil
import questionary

DPATH = os.path.join(os.path.dirname(__file__), "config/presets.txt")
CONF = jsload(open(os.path.join(os.path.dirname(__file__), "config/config.json")))
CREATION = CONF["creationPath"]
SAVING = CONF["savingPath"]

try:
    if CREATION == "pwd":
        CREATION = os.getcwd()
    elif not os.path.exists(CREATION):
        raise FileNotFoundError(f"Path '{CREATION}' does not exist, using working directory instead")
except FileNotFoundError as e:
    print(e)
    CREATION = os.getcwd()

try:
    if SAVING == "default":
        SAVING = DPATH
    elif not os.path.exists(SAVING):
        raise FileNotFoundError(f"Path '{SAVING}' does not exist, using default path instead")
except FileNotFoundError as e:
    print(e)
    SAVING = DPATH

if not os.path.exists(SAVING):
    print("File 'presets.txt' does not exist, creating it...")
    open(SAVING, "w").close()


PROJECTS = get_subdirectories(CREATION)
PRESETS = saved_presets(SAVING)

console = Console(theme=rich_theme)

# Additional functions for linting inputs
def pause(error_msg):
    """Pause the program and show an exception message"""
    console.print(error_msg, style="error")
    console.print("Press any key to continue...", end="", style="continue")
    os.system("bash -c 'read -r -n 1 -s'")
    os.system("clear")

def validate_folder_name(name):
    """Linting the name of the project introduced by the user"""
    if len(name) <= 0: 
        return "Write a name"
    
    for char in FORBIDDEN:
        if char in name:
            return f"Name contains an invalid character (`{char}`)"
        
    if name in PROJECTS:
        return f"File '{name}' already exists"
    
    return True

def validate_preset_name(preset):
    """Linting the name of the preset to be saved"""
    if len(preset) <= 0: 
        return "Write a name"
    
    if preset in PRESETS:
        return f"Preset '{preset}' already exists"
    
    return True

def validate_load(preset):
    """Linting the name of the preset to be loaded"""
    if not preset in PRESETS:
        return "Preset does not exist"
    
    return True

# Menu
os.system("clear")
while True:
    try:
        option = questionary.select(
            "Choose an option:",
            style = custom_style_fancy,
            instruction = "(Use arrow keys)",
            choices = ["1. Create a new Project",
                    "2. Save a Preset",
                    "3. Load a Preset",
                    "4. See Tree (Presets)",
                    "5. See Tree (Projects)",
                    "0. Salir"]
        ).ask(kbi_msg="Program interrupted...")
        
        if option == None or option[0] == "0": break

        match option[0]:
            case "1":
                name_project = questionary.text(
                    "Enter the name of the project",
                    style = custom_style_fancy, 
                    instruction = "(Ctrl+c to cancel)\n> ",
                    validate = validate_folder_name
                ).unsafe_ask()

                dir = f"{CREATION}/{name_project}"

                subfolder(CREATION, name_project, dir)
                PROJECTS.append(name_project)
                console.print(f"Project [magenta]{name_project}[/] successfully created", style="success")

            case "2":
                name_preset = questionary.text(
                    "Enter the name of the preset",
                    style = custom_style_fancy, 
                    instruction = "(Ctrl+c to cancel)\n> ",
                    validate = validate_preset_name
                ).unsafe_ask()

                new_preset(name_preset, SAVING)
                PRESETS.append(name_preset)

            case "3":
                if not PRESETS:
                    pause("There are no saved presets to load")
                    continue

                show_presets(SAVING)

                preset = questionary.text(
                    "Enter the name of the preset",
                    style = custom_style_fancy, 
                    instruction = "(Ctrl+c to cancel)\n> ",
                    validate = validate_load
                ).unsafe_ask()

                name = questionary.text(
                    "Enter the name of the project (preset will be loaded here)",
                    style = custom_style_fancy,
                    instruction = "(Ctrl+c to cancel)\n> ",
                    validate = validate_folder_name).unsafe_ask()

                load(SAVING, CREATION, name, preset)
                PROJECTS.append(name)
                console.print(f"Preset [magenta]{preset}[/] successfully loaded in [link file://{CREATION}/{name} magenta italic]{name}[/].",style="success")

            case "4":
                if not PRESETS:
                    pause("There are no saved presets to load")
                    continue

                show_presets(SAVING)

                name = ".tmp"
                dir = f"{CREATION}/{name}"
                tree = style_tree(dir)

                preset = questionary.text(
                    "Enter the name of the preset",
                    style = custom_style_fancy, 
                    instruction = "(Ctrl+c to cancel)\n> ",
                    validate = validate_load
                ).unsafe_ask()

                load(SAVING, CREATION, name, preset)
                walk_directory(dir, tree)
                shutil.rmtree(dir)

                console.print(tree)
                pause("\n*Note: you can click on folders to open them!")

            case "5":
                if not PROJECTS:
                    pause("There are no projects to be shown")

                name_project = questionary.select(
                    "Select a project",
                    style = custom_style_fancy,
                    instruction = "(Use arrow keys)",
                    choices = PROJECTS
                ).unsafe_ask()

                dir = f"{CREATION}/{name_project}"
                tree = style_tree(dir)

                walk_directory(dir, tree)
                console.print(tree)
                pause("\n*Note: you can click on folders to open them!")

    except KeyboardInterrupt:
        continue
    