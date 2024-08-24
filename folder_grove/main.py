from functions.subfolder import new_preset, subfolder, show_presets, saved_presets, load, FORBIDDEN
from functions.others import get_subdirectories, walk_directory, clean_screen, pause
from style import ascii_art_text, custom_style_fancy, rich_theme, style_tree, rainbow_text

import os
import shutil
import questionary
from rich.console import Console
from json import load as jsload
from urllib.parse import quote

clean_screen()

DPATH = os.path.join(os.path.dirname(__file__), "config/presets.txt")
CONF = jsload(open(os.path.join(os.path.dirname(__file__), "config/config.json")))
CREATION = CONF["creationPath"]
SAVING = CONF["savingPath"]

console = Console(theme=rich_theme)

# Getting project creation path
try:
    if CREATION == "pwd":
        CREATION = os.getcwd()
    elif not os.path.exists(CREATION):
        raise FileNotFoundError(f"Path '{CREATION}' does not exist, using working directory instead")
except FileNotFoundError as e:
    console.print(e, style="error")
    CREATION = os.getcwd()

# Getting presets file path
try:
    if SAVING == "default":
        SAVING = DPATH
    elif not os.path.exists(SAVING):
        raise FileNotFoundError(f"Path '{SAVING}' does not exist, using default path instead")
except FileNotFoundError as e:
    console.print(e, style="error")
    SAVING = DPATH

if not os.path.exists(SAVING):
    console.print("File 'presets.txt' does not exist. Creating file...", style="error")
    open(SAVING, "w").close()

PROJECTS = get_subdirectories(CREATION)
PRESETS = saved_presets(SAVING)

# Additional functions for validating input
def validate_folder_name(name):
    """Parses the name of the project and checks if it's valid"""
    if len(name) <= 0: 
        return "Write a name"
    
    for char in FORBIDDEN:
        if char in name:
            return f"Name contains an invalid character (`{char}`)"
        
    if name in PROJECTS:
        return f"File '{name}' already exists"
    
    return True

def validate_preset_name(preset):
    """Parses the name of the preset and checks if it's valid"""
    if len(preset) <= 0: 
        return "Write a name"
    
    if preset in PRESETS:
        return f"Preset '{preset}' already exists"
    
    return True

def validate_load(preset):
    """Parses the name of the preset to be loaded and checks if it exists"""
    if not preset in PRESETS:
        return "Preset does not exist"
    
    return True

# Menu
# console.print(f"[bold white]{ascii_art_text}[/]")
console.print(rainbow_text(ascii_art_text))

menu_choices = [
"1. Create a new Project",
"2. Save a Preset",
"3. Load a Preset",
"4. See Tree (Presets)\n",
"5. Clean Screen",
"0. Exit"
]

while True:
    try:
        option = questionary.select(
            "Choose an option:",
            style = custom_style_fancy,
            instruction = "(Use arrow keys)",
            choices = menu_choices
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

                console.print(f"Project [link file://{CREATION}/{quote(name_project)} italic magenta]{name_project}[/] successfully created", style="success")

            case "2":
                name_preset = questionary.text(
                    "Enter the name of the preset",
                    style = custom_style_fancy, 
                    instruction = "(Ctrl+c to cancel)\n> ",
                    validate = validate_preset_name
                ).unsafe_ask()

                new_preset(name_preset, SAVING)
                PRESETS.append(name_preset)

                console.print(f"Preset [magenta]{name_preset}[/] saved successfully", style="success")

            case "3":
                if not PRESETS:
                    pause("There are no saved presets to load")
                    continue

                show_presets(SAVING)

                preset = questionary.autocomplete(
                    "Enter the name of the preset:",
                    style = custom_style_fancy,
                    choices=PRESETS,
                    validate = validate_load
                ).unsafe_ask()

                name = questionary.text(
                    "Enter the name of the project (preset will be loaded here)",
                    style = custom_style_fancy,
                    instruction = "(Ctrl+c to cancel)\n> ",
                    validate = validate_folder_name).unsafe_ask()

                load(SAVING, CREATION, name, preset)
                PROJECTS.append(name)

                console.print(f"Preset [magenta]{preset}[/] successfully loaded in [link file://{CREATION}/{quote(name)} magenta italic]{name}[/].",style="success")

            case "4":
                if not PRESETS:
                    pause("There are no saved presets to load")
                    continue

                show_presets(SAVING)

                preset = questionary.autocomplete(
                    "Enter the name of the preset:",
                    style = custom_style_fancy,
                    choices=PRESETS,
                    validate = validate_load
                ).unsafe_ask()

                name = preset
                dir = f"{CREATION}/{name}"
                tree = style_tree(dir)

                load(SAVING, CREATION, name, preset)
                walk_directory(dir, tree)
                shutil.rmtree(dir)

                console.print(tree)
                pause("")
            
            case "5":
                clean_screen()
                console.print(rainbow_text(ascii_art_text))

    except KeyboardInterrupt:
        continue
    