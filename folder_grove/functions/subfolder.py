from style import custom_style_fancy, rich_theme
from rich.console import Console
import os
import questionary

FORBIDDEN = ".;{}=*^%$#@!~`´|\\<>?¿¡/\"\'"
console = Console(theme=rich_theme)

def validate_subfolders(subfolders):
    """Linting the name of the subfolders introduced by the user"""
    if not subfolders:
        return "You need to create at least one subfolder"
    
    for char in FORBIDDEN:
        if char in subfolders:
            return f"Subfolder name contains an invalid character ({char})"
    
    sub = list(filter(lambda x: x != '', subfolders.strip().split(',')))
    comas = subfolders.count(",")

    # Cannot have more comas than subfolders, that could lead to an error
    if comas >= len(sub):
        return "Type another subfolder or delete the comma (,)"
    
    
    
    return True


def subfolder(path, name, dir):
    """Non-persistent subfolder creation"""
    confirm = questionary.confirm(
        f"Do you want to create subfolders in {dir}?",
        default = False,
        instruction = "(y/N) ",
        style = custom_style_fancy
    ).ask()
    
    if confirm:
        subfolders = questionary.text(
            "Type the name of the subfolders (comma-separated)",
            style = custom_style_fancy,
            instruction = "(Example: doc,bin,headers,src)\n>",
            validate = validate_subfolders
        ).ask()
        
        array = subfolders.strip().split(',')
        for subfolder_name in array:
            new_dir = os.path.join(dir, subfolder_name.strip())
            os.makedirs(new_dir, exist_ok=True)
                
            if os.path.isdir(new_dir):
                subfolder(path, name, new_dir)

def new_preset(name_preset, saving):
    """Saves template to a file"""
    result = []
    
    
    def save_paths(cd):
        """Saves subfolder's paths in a list"""
        confirm = questionary.confirm(
            f"Do you want to save subfolders in {cd}?",
            default = False,
            instruction = ("(y/N) "),
            style = custom_style_fancy
        ).ask()
    
        if confirm:
            subfolders = questionary.text(
                "Type the name of the subfolders (comma-separated)",
                style=custom_style_fancy,
                instruction="(Example: doc,bin,headers,src)\n>",
                validate=validate_subfolders
            ).ask()
        else: 
            return
        
        array = subfolders.strip().split(',')

        for subfolder in array:
            new_cd = os.path.join(cd, subfolder).replace("\\", "/")
            result.append(new_cd)
            save_paths(new_cd)
    
    
    save_paths(f"/{name_preset}")
    with open(saving, "a") as file:
        file.write( "#" + name_preset + "\n")
        file.write( "/" + name_preset + "\n")
        
        for line in result:
            file.write(line + "\n")
        file.write("\n")
        file.close()

def load(save, create, name, preset):
    """Creates folder and subfolders following template pattern"""
    size = len(preset)+1
    
    new_dir = f"{create}/{name}"
    os.makedirs(new_dir)

    with open(save, "r") as file:
        for line in file:
            if line[:size] == "/" + preset:
                new_line = new_dir + line[size:].strip()
                os.makedirs(new_line, exist_ok=True)
        file.close()
        

def remove_preset(saving, preset):
    """Removes template from file."""
    
    with open(saving, "r") as file:
        lines = file.readlines()
    
    with open(saving, "w") as file:
        for line in lines:
            if not (line.startswith("#" + preset) or line.startswith("/" + preset)):
                file.write(line)


def saved_presets(saving):
    """Gets saved templates from file and keeps them in heap memory"""
    with open(saving, "r") as file:
        options = []
        for line in file:
            if line.startswith("#"):
                options.append(line[1:].strip())
        file.close()
    return options

def show_presets(saving):
    """Shows saved templates in heap memory"""
    presets = saved_presets(saving)
    console.print("Saved Templates:", style="bold #0f8994")
    
    for p in presets:
        console.print(p, end="    ", style="bold #21dbc9")
    print()
        