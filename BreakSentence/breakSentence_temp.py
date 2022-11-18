#--------------------------------------------#
#       Denotes - Break Setence API          #
#                                            #
#       識別句子界限在文字片段中的位置          #
#--------------------------------------------#

import requests, uuid, json, os, click,openpyxl
import pandas as pd



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
@click.option('--name', help="Input files name. e.g. --name testfile")
@click.option('--lang', help="Source language [en|zh-tw]. e.g. --lang en")
def cli(type, name, lang):
    global RootDIR
    global targetPath, outputPath
    global token,rowCount
    RootDIR = os.getcwd()
    if type == ".txt":
        token=1
        targetPath = os.chdir(RootDIR+ f"/BreakSentence_Input/Text")
        target= str(RootDIR+ f"/BreakSentence_Input/Text")+ f"/{name}{type}"
        outputPath = RootDIR + f"/BreakSentence_Output/Text/{name}{type}"
        readtextFile(target)
    elif type == ".xlsx":
        token=2
        global workbook
        targetPath = os.chdir(RootDIR+ f"/BreakSentence_Input/Excel")
        target= str(RootDIR+ f"/BreakSentence_Input/Excel")+ f"/{name}{type}"
        outputPath = RootDIR + f"/BreakSentence_Output/Excel/{name}{type}"
        readExcelFile(target,lang)
        workbook = openpyxl.Workbook()
        workbook.save(outputPath)
        rowCount=0

def writetextFile(SentenceSet: list):
    ## Write the segmented sentence to files.
    with open(outputPath,'a') as f:
        for set in SentenceSet:
            f.write(f"{set}\n")
    

def writeExcelFile(SentenceSet: list):
    ## Write the segmented sentence to files.
    global rowCount
    wb = openpyxl.load_workbook(outputPath)
    workSheet = wb.active

    # write value from list to excel file
    for i in range(0,len(SentenceSet)):
        workSheet[rowCount+1+i][0].value =  SentenceSet[i]
    rowCount += len(SentenceSet)
    wb.save(outputPath)


def readtextFile(target):
    ## Read source files from certain directory.
    global Set
    Set=[]
    with open(target,'r') as f:
        for line in f:
            Set.append(line.strip('\n\t').split(',')[0])
    print(f"\n-------------------------[  Read Text File  ]----------------------------------\n")
    print(Set)

    
def readExcelFile(target,lang):
    ## Read source files from certain directory.
    global sheetSet, ps, Set
    sheetSet = []
    Set=[]
    colNum  = 0
    files = target
    data = pd.ExcelFile(files)
    ps = openpyxl.load_workbook(files)
    # Get all sheet
    for sheet in range(0,len(ps.worksheets)):
        sheetSet.append(ps[data.sheet_names[sheet]])
    
    # Get target column number
    for i in range(0,len(sheetSet)):
        for col in range(0,len(sheetSet[i][1])):
            if lang ==("en" or "EN"):
                if sheetSet[i][1][col].value == ("en" or "EN"):
                    colNum = col
            elif lang ==("zh-tw" or "ZH-TW" or "ZH" or "zh"):
                if sheetSet[i][1][col].value == ("zh-tw" or "ZH-TW" or "ZH" or "zh"):
                    colNum = col
         # Format to List
        for row in range(2,sheetSet[i].max_row+1):
            print(f"-------SheetIndex{i}--ROW:{row}-------\n")
            Set.append(sheetSet[i][row][colNum].value)
    print(f"len:{len(Set)}")


@cli.command()
def run():
    '''Get the sentence boarder by using Azure BreakSentenceAPIv3.'''
    
    for requestIndex in range(0,len(Set)):
        OutputSet=[]
        body = [{
            'text': Set[requestIndex]
        }]
        print("------------------[Sending Requests ]--------------------------------")
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        print("------------------[Receive Response ]--------------------------------")
        print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
        BreakSentence = (response[0]["sentLen"])
        print(f"\n")
        for breakNum in BreakSentence:
            OutputSet.append(''.join(Set[requestIndex][x] for x in range(len(Set[requestIndex])) if x < breakNum))
            Set[requestIndex] = ''.join(Set[requestIndex][x] for x in range(len(Set[requestIndex])) if x >= breakNum)
        print(OutputSet)
        if token==1:
            writetextFile(OutputSet)
        elif token==2:
            writeExcelFile(OutputSet)
        OutputSet=[]

if __name__ == '__main__':
    cli()







