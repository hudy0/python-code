import requests
from pprint import pprint

response = requests.get('https://peps.python.org/api/peps.json')
data = response.json()
pprint([(k, v['title']) for k, v in data.items()][:10])
