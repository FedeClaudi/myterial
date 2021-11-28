
from rich import print
from rich.columns import Columns
from rich.panel import Panel
from rich.box import SIMPLE_HEAVY

from typing import Tuple

from myterial.lookup import colors


base_colors = sorted([
    'red', 'pink', 'purple', 'deep_purple', 'indigo', 'blue', 
    'light_blue', 'cyan', 'teal', 'green', 'light_green', 'lime',
    'yellow', 'amber', 'orange', 'salmon', 'brown', 'grey', 
    'blue_grey', 'black', 'white'
])

suffixes = ( '_lighter', '_darker', '_light', '_dark', )


def strip(color:str) -> str:
    for suff in suffixes:
        color = color.replace(suff, '')
    return color


panels = []
for cstem in base_colors:
    colors_group = {k:c for k,c in colors.items() if strip(k) == cstem }
    panels.append(
        Panel(
            '\n'.join([f'[{code}] ▶ {name}' for name, code in colors_group.items()]),
            # title=f'[b {list(colors_group.values())[0]}]{cstem}', 
            # border_style=None,
            box = SIMPLE_HEAVY,
            width=28, 
            height=7,
        )
    )


print(Panel.fit(Columns(panels), title='myterial colors'))