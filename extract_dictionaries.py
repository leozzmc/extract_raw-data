from audioop import add
from itertools import count
import os, re
import openpyxl
import pandas as pd
from string import digits

#---------- Billingual Corpus (for Azure) ---------#
# Dictionary-1
class Dictionary1:

    def __init__(self):
        global ROOTDIR 
        ROOTDIR = os.getcwd()
        print(ROOTDIR)
    
    def get_execel_file(self,DictionaryPath):
        global sheet, output
        # files = ROOTDIR +  "/Dictionary/01-佛學辭典.xlsx"
        files = ROOTDIR +  str(DictionaryPath)
        # Load orgin dictionary-1 excel file
        data = pd.ExcelFile(files)
        ps = openpyxl.load_workbook(files)
        # Save to another excel file
        ps.save('output_dic1.xlsx')
        output = openpyxl.load_workbook('output_dic1.xlsx')
        sheet = output[data.sheet_names[0]]

    # Iterate the sheet fields by rows and cols.
    # to sheet.max_row
    def ProcessSheet(self,DictionaryPath):
        self.get_execel_file(DictionaryPath)
        for row in range(1,sheet.max_row):
            for col in range(0, sheet.max_column):
                print(f"---------------------------------Row:{row} Col:{col}------------------------------------")
                # Delete Null items, that is delete fields without Tibetan definition.
                if sheet[row][1].value is None:
                    sheet.delete_rows(row)
                # Regular Expression for Chinese strings in the brackets
                string = str(sheet[row][2].value)
                # 全形括號
                if '（' in string: 
                    print(string)
                    p1 = re.compile(r'[（](.*?)[）]', re.S)
                    # find all match item and store in a list r1
                    r1 = re.findall(p1, string)
                    print(f"Match Results: {r1}")
                    # Process the list, delete numbers, such as '1895-1922', '1895一1922'...etc
                    for i in range(0,len(r1)):
                        new_item = re.sub(r'[0-9,"─","一","—"]+','',r1[i])
                        r1[i]= new_item          
                    print(f"New Results: {r1}")
                    # Delete Chinese strings in the brackets //刪除括號內中文
                    new_string = string
                    for i in r1:
                        new_string = re.sub(f"（{i}）","",new_string)                    
                    sheet[row][2].value = new_string
                    print(f"-------Results: {sheet[row][2].value}----")

        # Save the change.
        output.save('output_dic1.xlsx')


class Dictionary2:

    def __init__(self):
        global ROOTDIR 
        ROOTDIR = os.getcwd()
        print(ROOTDIR)

    def get_execel_file(self,DictionaryPath):
        global sheet, output
        # /Dictionary/02-漢藏對照佛學辭典.xlsx
        #files = ROOTDIR +  str(DictionaryPath)
        files = ROOTDIR +  "/Dictionary/02-漢藏對照佛學辭典.xlsx"
        data = pd.ExcelFile(files)
        ps = openpyxl.load_workbook(files)
        ps.save('output_dic2.xlsx')
        output = openpyxl.load_workbook('output_dic2.xlsx')
        sheet = output[data.sheet_names[0]]
        
    
    # Iterate the sheet fields by rows and cols.
    def ProcessSheet(self,DictionaryPath):
        self.get_execel_file(DictionaryPath)
        RowLimit = sheet.max_row
        for row in range(1,RowLimit):
            termination_symbol_counter=0
            Tibetan_WordGroup = []
            Tibetan_List = []
            for col in range(0, sheet.max_column):
                print(f"---------------------------------Row:{row} Col:{col}------------------------------------")
                # ----------------- (1) copy Chinese word-----------------------#
                if sheet[row][0].value is None:
                    sheet[row][0].value = sheet[row-1][0].value 
               
                # --------------(2) Tibetan words group seperations----------------------#
                # Check the numbers of termination symbol '།'
                for i in str(sheet[row][col].value):
                    if i == '།':
                        termination_symbol_counter = termination_symbol_counter +1
                # Split the words in a group
                if termination_symbol_counter > 1:
                    Tibetan_WordGroup = sheet[row][1].value.split(" ")
                    print(f"Tibtean Group List: {Tibetan_WordGroup}")
                    # Store in tuples
                    #sheet.insert_rows(len(Tibetan_WordGroup))
                    for j in Tibetan_WordGroup:
                        # Store in tuples
                        Tibetan_List.append((sheet[row][0].value,j))
                    print(f"Tibetan List: {Tibetan_List}")
                    # Insert multiple rows before next row.
                    sheet.insert_rows(row+1,len(Tibetan_List))
                    termination_symbol_counter = 0
                 # ------------------ (3) Delete words in the brackets-------------------#
                string = str(sheet[row][2].value)
                if ('（' or '〔'or '）' or '〕')in string:
                    #print(string)
                    p1 = re.compile(r'[（,〔](.*?)[）,〕]', re.S)
                    r1 = re.findall(p1, string)
                    #print(f"Match Results: {r1}")
                    # Delete Chinese strings in the brackets 
                    new_string = string
                    for i in r1:
                        new_string = re.sub(f"（{i}）|〔{i}〕","",new_string)                    
                    sheet[row][2].value = new_string
                    #print(f"-------Results: {sheet[row][2].value}----")
            
                if len(Tibetan_List) > 0:
                    sheet.delete_rows(row)
                    # sheet[row][0].value = Tibetan_List[0][0]
                    # sheet[row][1].value = Tibetan_List[0][1]
                    # sheet[row+1][0].value = Tibetan_List[1][0]
                    # sheet[row+1][1].value = Tibetan_List[1][1]
                    for addrow in range(0,len(Tibetan_List)):
                        sheet[row + addrow][0].value = Tibetan_List[addrow][0]
                        sheet[row + addrow][1].value = Tibetan_List[addrow][1]
                    RowLimit = RowLimit + len(Tibetan_List)

        output.save('output_dic2.xlsx')


if __name__ == '__main__':
    # Dic1 = Dictionary1()
    # DicPath = str(input("Enter Dictionary File Path: "))
    # Dic1.ProcessSheet(DicPath)
    Dic2 = Dictionary2()
    DicPath = str(input("Enter Dictionary File Path: "))
    Dic2.ProcessSheet(DicPath)














#--------- Billingual Dictionary ---------#

## Dictionary-2
## Dictionary-3

## Dictionary-1
## Dictionary-4
## Dictionary-5
## Dictionary-6
