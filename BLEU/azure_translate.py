import requests, uuid, json

# Add your key and endpoint
key = "939ac55c5a914a9e9745a38f2f44ec33"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "eastasia"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'zh-tw',
    'to': 'en'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': '你好嗎'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()
print(response[0]["translations"][0]["text"])
# print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))