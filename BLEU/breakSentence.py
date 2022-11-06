#--------------------------------------------#
#       Denotes - Break Setence API          #
#                                            #
#       識別句子界限在文字片段中的位置          #
#--------------------------------------------#

import requests, uuid, json

# Add your key and endpoint
key = "939ac55c5a914a9e9745a38f2f44ec33"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "eastasia"

path = '/BreakSentence'
constructed_url = endpoint + path

params = {
    'api-version': '3.0'
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
Set=['本書主要內容是怙主 敦珠仁波切的一系列開示。這當中最早的乃紀錄於一九六二年，其餘大部分開示則是於一九七零年間分別在東、西方國家所講授。這些談話經由錄音、繕寫後，推測是在加德滿都以小量印行。在敦珠仁波切佛母敦珠．桑嫞．仁增．旺嫫的囑咐下，將其中一本交付蓮師翻譯小組以利後續翻譯。感恩佛母仁慈的允諾，讓西方讀者得以接觸這些甚妙法教。']
OutputSet=[]

body = [{
    'text': '本書主要內容是怙主 敦珠仁波切的一系列開示。這當中最早的乃紀錄於一九六二年，其餘大部分開示則是於一九七零年間分別在東、西方國家所講授。這些談話經由錄音、繕寫後，推測是在加德滿都以小量印行。在敦珠仁波切佛母敦珠．桑嫞．仁增．旺嫫的囑咐下，將其中一本交付蓮師翻譯小組以利後續翻譯。感恩佛母仁慈的允諾，讓西方讀者得以接觸這些甚妙法教。'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
BreakSentence = (response[0]["sentLen"])
#print(BreakSentence)
print(Set[0])
#print(Set[0][0:22])
print(f"\n")
for breakNum in BreakSentence:
    OutputSet.append(''.join(Set[0][x] for x in range(len(Set[0])) if x < breakNum))
    Set[0] = ''.join(Set[0][x] for x in range(len(Set[0])) if x >= breakNum)
    print(Set[0])
    print(f"\n")
print(OutputSet)
