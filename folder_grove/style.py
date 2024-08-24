from questionary import Style
from rich.theme import Theme
from rich.tree import Tree
from rich.text import Text
from rich.style import Style as richStyle

ascii_art_text = f""" ____  _____  __    ____  ____  ____     ___  ____  _____  _  _  ____ 
( ___)(  _  )(  )  (  _ \\( ___)(  _ \\   / __)(  _ \\(  _  )( \\/ )( ___)
 )__)  )(_)(  )(__  )(_) ))__)  )   /  ( (_-. )   / )(_)(  \\  /  )__) 
(__)  (_____)(____)(____/(____)(_)\_)   \\___/(_)\_)(_____)  \\/  (____)

               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\\88/8o
   ,%&\\%&&%&&%,@@@\\@@@/@@@88\\88888/88'
   %&&%&%&/%&&%@@\\@@/ /@@@88888\\88888'
   %&&%/ %&%%&&@@\\ V /@@' ` `/88'
   ` ` /%&'    |.|        \\ '|8'
       |o|        | |         | |
       |.|        | |         | |
 \\\\/ ._\\//_/__/  ,\\_//__\\\\/.  \\_//__/_ 
"""

rich_theme = Theme({
    "success" : "bold green",
    "error": "bold red",
    "continue": "#fff9a8"
})

custom_style_fancy = Style([
    ('qmark', 'fg:#673ab7 bold'),       # token in front of the question
    ('question', 'bold'),               # question text
    ('answer', ''),                     # submitted answer text behind the question
    ('pointer', 'fg:#673ab7 bold'),     # pointer used in select and checkbox prompts
    ('highlighted', 'fg:#673ab7 bold'), # pointed-at choice in select and checkbox prompts
    ('selected', 'fg:#cc5454'),         # style for a selected item of a checkbox
    ('separator', 'fg:#cc5454'),        # separator in lists
    ('instruction', 'fg:#00d18b bold'), # user instructions for select, rawselect, checkbox
    ('text', ''),                       # plain text
    ('disabled', 'fg:#858585 italic')   # disabled choices for select and checkbox prompts
])

def style_tree(dir) -> Tree:
    """Builds styled tree root"""
    return Tree(
    Text(dir, style="bold light_salmon3"),
    guide_style="bold bright_blue"
)

def rainbow_text(text):
    """Generates text with rainbow effect"""
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    styled_text = Text()
    color_index = 0

    for char in text:
        styled_text.append(char, style=richStyle(color=colors[color_index]))
        color_index = (color_index + 1) % len(colors)

    return styled_text