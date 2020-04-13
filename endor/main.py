import requests
import prettyconf
from loadlevels import LoadLevel, get_load_level

API_URL = prettyconf.config('API_URL')
STYLE_FORMAT = 'font=AndaleMono size=13'
DEFAULT_COLOR = 'white'
TITLE = 'endor'


r = requests.get(API_URL)
stats = r.json()
output = []
output.append(TITLE + ' | color={title_color}')
output.append('---')
critical = False
for key, value in stats.items():
    current_value = value['current']
    max_value = value['max']
    units = value['units']
    display = f'{key}: {round(current_value)}{units}'
    color = DEFAULT_COLOR
    if max_value != -1:
        percent = round(current_value * 100 / max_value)
        loadlevel = get_load_level(percent)
        critical = loadlevel == LoadLevel.CRITICAL
        color = loadlevel.value
        if units != '%':
            display += f'/{max_value:.0f}{units} ({percent}%)'
    output.append(f'{display} | {STYLE_FORMAT} color={color}')

title_color = LoadLevel.CRITICAL.value if critical else DEFAULT_COLOR
print('\n'.join(output).format(title_color=title_color))
