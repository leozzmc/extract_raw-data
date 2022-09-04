import os, re
import openpyxl
import pandas as pd
from string import digits

#---------- Billingual Corpus (for Azure) ---------#
## Dictionary-1
## 1. Read Excel Files
ROOTDIR = os.getcwd()
print(ROOTDIR)
#files = ROOTDIR +  input("Enter the Excel files path:")
files = ROOTDIR +  "/Dictionary/01-佛學辭典.xlsx"
data = pd.ExcelFile(files)
ps = openpyxl.load_workbook(files)
ps.save('output.xlsx')
output = openpyxl.load_workbook('output.xlsx')
sheet = output[data.sheet_names[0]]
print(sheet)

## 2. Output Directories and Excel Files


print(sheet.title, sheet.max_row, sheet.max_column)

# to sheet.max_row
for row in range(1,sheet.max_row):
    for col in range(0, sheet.max_column):
        if sheet[row][2] is not None:
            print(f"---------------------------------Row:{row} Col:{col}------------------------------------")
            # Delete Null items
            if sheet[row][1].value is None:
                sheet.delete_rows(row)
            # Regular Expression for Chinese strings //判斷括號中是否有中文
            string = str(sheet[row][2].value)
            # 全形括號
            if '（' in string: 
                print(string)
                p1 = re.compile(r'[（](.*?)[）]', re.S)
                # find all match item and store in a list
                r1 = re.findall(p1, string)
                print(f"Match Results: {r1}")
                for i in range(0,len(r1)):
                    new_item = re.sub(r'[0-9,"─","一","—"]+','',r1[i])
                    r1[i]= new_item
                    
                print(f"New Results: {r1}")            
            # Delete Chinese strings in the brackets //刪除括號內中文
                A =0
                new_string = string
                for i in r1:
                    new_string = re.sub(f"（{i}）","",new_string)
                    A=A+1
                    #print(f"{A}:{new_string}\n")
                    
                sheet[row][2].value = new_string
                print(f"-------Results: {sheet[row][2].value}----")
        else:
            output.save('output.xlsx')
















#--------- Billingual Dictionary ---------#

## Dictionary-2
## Dictionary-3

## Dictionary-1
## Dictionary-4
## Dictionary-5
## Dictionary-6
