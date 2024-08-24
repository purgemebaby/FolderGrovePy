from questionary import Style
from rich.theme import Theme
from rich.tree import Tree
from rich.text import Text
from urllib.parse import quote

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

# Función para construir la raiz del arbol con estilo
def style_tree(dir) -> Tree:
    return Tree(
    Text(dir, style=f"link file://{quote(dir)} bold light_salmon3"),
    guide_style="bold bright_blue"
)