import os, re
import openpyxl
import pandas as pd

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

for row in range(1,60):
    for col in range(0, sheet.max_column):
        print(f"------------------Row:{row} Col:{col}----------------------")
        # Delete Null items
        # if sheet[row][1].value is None:
        #     sheet.delete_rows(row)
        # Regular Expression for Chinese strings //判斷括號中是否有中文
        string = str(sheet[row][2].value)
        if '（' in string: 
            print(string)
            p1 = re.compile(r'[（](.*?)[）]', re.S)
            r1 = re.findall(p1, string)
            print(type(r1[0]))
            print(f"Match Results: {r1}")

        # Delete Chinese strings in the brackets //刪除括號內中文
        # if sheet[row][2].value:
        #     pass
#output.save('output.xlsx')
















#--------- Billingual Dictionary ---------#

## Dictionary-2
## Dictionary-3

## Dictionary-1
## Dictionary-4
## Dictionary-5
## Dictionary-6
