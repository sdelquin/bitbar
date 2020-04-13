import requests
import prettyconf

API_URL = prettyconf.config('API_URL')

r = requests.get(API_URL)
stats = r.json()
print('endor')
print('---')
for key, value in stats.items():
    current_value = value['current']
    max_value = value['max']
    units = value['units']
    display = f'{key}: {current_value:.2f}{units}'
    if max_value != -1 and units != '%':
        percent = round(current_value * 100 / max_value)
        display += f'/{max_value:.0f}{units} ({percent}%)'
    print(f'{display} | font=AndaleMono size=13')
