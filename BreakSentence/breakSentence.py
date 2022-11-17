#--------------------------------------------#
#       Denotes - Break Setence API          #
#                                            #
#       識別句子界限在文字片段中的位置          #
#--------------------------------------------#

import requests, uuid, json, os

# Add your key and endpoint
key = os.environ["AZURE_API_KEY1"]
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
location = os.environ["AZURE_LOCATION"]

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
Set=['而這又代表了什麼？我們當中無有一人未曾領受尊者的法教與灌頂。我們現在都因佛法與尊者有了連結，因此我們必須持守三昧耶。倘若只用嘴上的虔敬四處說著：「嘉華仁波切，嘉華仁波切 ！」但行為上卻違背這份虔敬，那就是徹底錯誤的行為。我們必須依循尊者的希願而為。把三昧耶濃縮為一，務必知道我們都是佛陀的弟子、都是佛陀的追隨者。原則上我們應該修行自己依循的傳統，同時也不批評其他傳統和派別、不嘲笑他人的過錯。身在國外的我們，不應展示自己的不當行為！即使無法對他人生起淨觀，我們最起碼也要決心且發願不批判他人、不對彼此生起邪見。有時我們簡直是在到處挑釁！一波未平一波又起，完全不得安寧！一定要盡力避免這些狀況。年長者應告誡年少者，我們都應該要提振精神、發起願心，在當前此刻這一點非常重要，實際上這就是為尊者祈願長壽，以及真正承事佛法的最佳方法。']
OutputSet=[]

body = [{
    'text': '而這又代表了什麼？我們當中無有一人未曾領受尊者的法教與灌頂。我們現在都因佛法與尊者有了連結，因此我們必須持守三昧耶。倘若只用嘴上的虔敬四處說著：「嘉華仁波切，嘉華仁波切 ！」但行為上卻違背這份虔敬，那就是徹底錯誤的行為。我們必須依循尊者的希願而為。把三昧耶濃縮為一，務必知道我們都是佛陀的弟子、都是佛陀的追隨者。原則上我們應該修行自己依循的傳統，同時也不批評其他傳統和派別、不嘲笑他人的過錯。身在國外的我們，不應展示自己的不當行為！即使無法對他人生起淨觀，我們最起碼也要決心且發願不批判他人、不對彼此生起邪見。有時我們簡直是在到處挑釁！一波未平一波又起，完全不得安寧！一定要盡力避免這些狀況。年長者應告誡年少者，我們都應該要提振精神、發起願心，在當前此刻這一點非常重要，實際上這就是為尊者祈願長壽，以及真正承事佛法的最佳方法。'
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
