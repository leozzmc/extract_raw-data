from itertools import count
from typing import List
import requests, uuid, json
import os, re
import openpyxl
import pandas as pd
import time

ReferenceDataPath=[
    "/EN-Dictionary/DR詞彙解釋.xlsx",
    "/EN-Dictionary/GP詞彙解釋.xlsx",
    "/EN-Dictionary/HL詞彙解釋.xlsx",
    "/EN-Dictionary/ML詞彙表.xlsx",
    "/EN-Dictionary/MP辭彙說明.xlsx",
    "/EN-Dictionary/T詞彙解釋.xlsx",
    "/EN-Dictionary/TGSM引用文典對照表.xlsx",
    "/EN-Dictionary/TGSM詞彙選列對照表.xlsx",
    "/EN-Dictionary/二十一度母 _ 八救難母 _ 詞彙表.xlsx"
]

#Add your key and endpoint
key = "*********"
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

class Excel_Data:

    def __init__(self):
        global ROOTDIR 
        ROOTDIR = os.getcwd()
        print(ROOTDIR)

    def get_execel_file(self,DataPath):
        global sheet, ps
        # files = ROOTDIR +  "/../EN-Dictionary/DR詞彙解釋.xlsx"
        files = ROOTDIR +  DataPath
        data = pd.ExcelFile(files)
        ps = openpyxl.load_workbook(files)
        # Get first sheet
        sheet = ps[data.sheet_names[0]]

    def ProcessSheet(self, DataPath,count):
        global OutputList
        OutputList= []
        self.get_execel_file(DataPath)
        for row in range(2,sheet.max_row+1):
            if sheet[row][0].value is not None:     
                body = [{
                        'text': f'{sheet[row][0].value}'
                    }]
                request = requests.post(constructed_url, params=params, headers=headers, json=body)
                response = request.json()
                print(response[0]["translations"][0]["text"])
                #print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
                sheet[row][2].value = response[0]["translations"][0]["text"]
                time.sleep(1)
        ps.save(f"azure_output_{count}.xlsx")



if __name__ == '__main__':
    ex = Excel_Data()
    counter=1
    for i in ReferenceDataPath:
        print(counter)
        ex.ProcessSheet(i,counter)
        counter+=1
