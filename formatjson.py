import json

import requests


response_API = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces')
data = json.loads(response_API.text)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
#jprint(response_API.json())
#print response_API.json()
#print response_API.text
#print response_API.status_code
#print response_API.headers
#print response_API.encoding
#print response_API.content
#print response_API.raw
#print response_API.url
#print response_API.history
#print response_API.elapsed
#print response_API.request
print(response_API.request)
#print response_API.cookies

