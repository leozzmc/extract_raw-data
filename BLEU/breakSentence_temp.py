#--------------------------------------------#
#       Denotes - Break Setence API          #
#                                            #
#       識別句子界限在文字片段中的位置          #
#--------------------------------------------#

import requests, uuid, json, os, click, sys

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
@click.option('--file', help="Input files name. e.g. --name testfile")
def cli(type, name):
    global RootDIR
    global targetPath, outputPath
    global token
    file=[]
    RootDIR = os.getcwd()
    # 要做到指定檔名
    if type == ".txt":
        token=1
        targetPath = os.chdir(RootDIR+ f"/BreskSentence_Input/Text/{name}")
        outputPath = RootDIR + f"/BreakSentence/Text/{name}"
        readtextFile()
    elif type == ".xlsx":
        token=2
        targetPath = os.chdir(RootDIR+ f"/BreskSentence_Input/Excel/{name}")
        outputPath = RootDIR + f"/BreakSentence/Excel/{name}"
        readExcelFile()
    pass

def writetextFile(SentenceSet: list):
    ## Write the segmented sentence to files.
    # outputPath
    pass

def writeExcelFile(SentenceSet: list):
    ## Write the segmented sentence to files.
    # outputPath
    pass

def readtextFile():
    ## Read source files from certain directory.
    with open(targetPath,'r') as f:
        result=[]
        with open('accounts.txt','r') as f:
            for line in f:
                result.append(line.strip('\n').split(',')[0])
        print(result)

    
def readExcelFile():
    ## Read source files from certain directory.
    # targetPath
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
    if token==1:
        writetextFile(OutputSet)
    elif toekn==2:
        writeExcelFile(OutputSet)

if __name__ == '__main__':
    cli()








