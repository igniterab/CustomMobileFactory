import requests
import json
from constants import HOST, PORT

#change components to try other codes
data = { "components": ["I","A","D","F","K"] }

try:
    response = requests.post(f"http://{HOST}:{PORT}", json=data)
    print(response.json())
except Exception as e:
    print(e)