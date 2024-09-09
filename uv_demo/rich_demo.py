# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
from rich.pretty import pprint


response = requests.get('https://peps.python.org/api/peps.json')
data = response.json()
pprint([(k, v['title']) for k, v in data.items()][:10])
