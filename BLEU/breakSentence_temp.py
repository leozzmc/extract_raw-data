#--------------------------------------------#
#       Denotes - Break Setence API          #
#                                            #
#       識別句子界限在文字片段中的位置          #
#--------------------------------------------#

import requests, uuid, json, os, click

# Get API Key and endpoints from environment variables
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

@click.group()
@click.option('--type', help="Input files types: [.txt|.xlsx] e.g. --type .txt, --type .xlsx")
def cli(type):
    global RootDIR
    global targetPath, outputPath
    RootDIR = os.getcwd()
    if type == ".txt":
        targetPath = os.chdir(RootDIR+ "/BreskSentence_Input/Text/")
    elif type == ".xlsx":
        targetPath = os.chdir(RootDIR+ "/BreskSentence_Input/Excel/")
    pass

def writeFile(SentenceSet: list):
    ## Write the segmented sentence to files.
    pass

def readFile():
    ## Read source files from certain directory.
    pass

@cli.command()
def run(sourceList: list):
    '''Get the sentence boarder by using Azure BreakSentenceAPIv3.'''
    Set=sourceList
    body = [{
        'text': Set[0]
    }]

    OutputSet=[]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    BreakSentence = (response[0]["sentLen"])
    print(Set[0])
    print(f"\n")
    for breakNum in BreakSentence:
        OutputSet.append(''.join(Set[0][x] for x in range(len(Set[0])) if x < breakNum))
        Set[0] = ''.join(Set[0][x] for x in range(len(Set[0])) if x >= breakNum)
    print(OutputSet)
    writeFile(OutputSet)

if __name__ == '__main__':
    cli()








