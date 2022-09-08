from itertools import count
import os, re
import openpyxl
import pandas as pd



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
        sheet.delete_cols(3) 
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
                    for j in Tibetan_WordGroup:
                        # Store in tuples
                        Tibetan_List.append((sheet[row][0].value,j))
                    print(f"Tibetan List: {Tibetan_List}")
                    # Insert multiple rows before next row.
                    sheet.insert_rows(row+1,len(Tibetan_List))
                    termination_symbol_counter = 0
                
            
                if len(Tibetan_List) > 0:
                    sheet.delete_rows(row)
                    for addrow in range(0,len(Tibetan_List)):
                        sheet[row + addrow][0].value = Tibetan_List[addrow][0]
                        sheet[row + addrow][1].value = Tibetan_List[addrow][1]
                        #sheet[row + addrow][2].value = Tibetan_List[addrow][2]
                    RowLimit = RowLimit + len(Tibetan_List)

                # ------------------ (3) Delete words in the brackets-------------------#
                # string = str(sheet[row][2].value)
                # if ('（' or '〔' or '(' or '[' or '）' or '〕' or ')' or ']')in string:
                #     #print(string)
                #     p1 = re.compile(r'[（〔(\[](.*?)[）〕)\]]', re.S)
                #     r1 = re.findall(p1, string)
                #     print(f"Match Results: {r1}")
                #     # Delete Chinese strings in the brackets 
                #     new_string = string
                #     for i in r1:
                #         # new_string = re.sub(f"（{i}）|〔{i}〕|({i})|[{i}]","",new_string)
                #         new_string = re.sub(r"[（〔(\[](.*?)[）〕)\]]","",new_string)
                #         new_string = re.sub(r"[（〔(\[](.*?)[）〕)\]]","",new_string)             
                #     sheet[row][2].value = new_string
                #     print(f"-------Results: {sheet[row][2].value}----")
        output.save('output_dic2.xlsx')


class Dictionary3:

    def __init__(self):
        global ROOTDIR 
        ROOTDIR = os.getcwd()
        print(ROOTDIR)
    
    def get_execel_file(self,DictionaryPath):
        global sheet, output
        # /Dictionary/03-翻譯名義集 藏梵漢英.xlsx
        #files = ROOTDIR +  str(DictionaryPath)
        files = ROOTDIR +  "/Dictionary/03-翻譯名義集 藏梵漢英.xlsx"
        data = pd.ExcelFile(files)
        ps = openpyxl.load_workbook(files)
        ps.save('output_dic3.xlsx')
        output = openpyxl.load_workbook('output_dic3.xlsx')
        sheet = output[data.sheet_names[0]]
    
    def ProcessSheet(self,DictionaryPath):
        self.get_execel_file(DictionaryPath)
        global RowLimit
        RowLimit = sheet.max_row
        # delete uneeded cols
        sheet.delete_cols(4)
        sheet.delete_cols(4)
        sheet.delete_cols(4)
        sheet.delete_cols(4)
        for row in range(1,RowLimit):
            termination_symbol_counter=0
            Chinese_WordGroup = []
            Chinese_List = []  
            for col in range(0, sheet.max_column):
                print(f"---------------------------------Row:{row} Col:{col}------------------------------------") 
                # --------------(1) Chinese words group seperations----------------------#
                # Check the numbers of termination symbol ','
                for i in str(sheet[row][2].value):
                    if i == '，':
                        print(str(sheet[row][2].value))
                        termination_symbol_counter = termination_symbol_counter +1
                # Split the words in a group
                if termination_symbol_counter > 1:
                    Chinese_WordGroup = sheet[row][2].value.split("，")
                    print(f"Chinese Group List: {Chinese_WordGroup}")
                    # Store in tuples
                    for j in Chinese_WordGroup:
                        # Store in tuples
                        Chinese_List.append((sheet[row][0].value,sheet[row][1].value,j))
                    print(f"Chinese List: {Chinese_List}")
                    # Insert multiple rows before next row.
                    sheet.insert_rows(row,len(Chinese_List)+1)
                    termination_symbol_counter = 0
                
               
                if len(Chinese_List) > 0:
                    sheet.delete_rows(row)
                    for addrow in range(0,len(Chinese_List)):
                        sheet[row + addrow][0].value = Chinese_List[addrow][0]
                        sheet[row + addrow][1].value = Chinese_List[addrow][1]
                        sheet[row + addrow][2].value = Chinese_List[addrow][2]
                    RowLimit = RowLimit + len(Chinese_List)
            # ----------------- (2) copy Tibetan word-----------------------#
            if sheet[row][0].value is None:
                sheet[row][0].value = sheet[row-1][0].value 
        
        for row in range(1, sheet.max_row):
            for col in range(0,sheet.max_column):
                print(f"---------------------------------Row:{row} Col:{col}------------------------------------")      
                # ------------------ (3) delete words in the brackets -----------#
                string = str(sheet[row][col].value)
                if '(' in string:
                    print(string)
                    p1 = re.compile(r'[(](.*?)[)]', re.S)
                    r1 = re.findall(p1, string)
                    print(f"Match Results: {r1}")
                    # Delete Chinese strings in the brackets 
                    new_string = string
                    for i in r1:
                        new_string = re.sub(r"[(](.*?)[)]","",new_string)           
                    sheet[row][col].value = new_string
                    print(f"-------Results: {sheet[row][col].value}----")
                  
        output.save('output_dic3.xlsx')
 


class Dictionary4:

    def __init__(self):
        global ROOTDIR 
        ROOTDIR = os.getcwd()
        print(ROOTDIR)
    
    def get_execel_file(self,DictionaryPath):
        global sheet, output
        # /Dictionary/04-藏汉常用合稱辭典.xlsx
        #files = ROOTDIR +  str(DictionaryPath)
        files = ROOTDIR +  "/Dictionary/04-藏汉常用合稱辭典.xlsx"
        data = pd.ExcelFile(files)
        ps = openpyxl.load_workbook(files)
        ps.save('output_dic4.xlsx')
        output = openpyxl.load_workbook('output_dic4.xlsx')
        sheet = output[data.sheet_names[0]]
    
    # Bilingual Corpus, that is to merge tibetan columns,then output files for Azure.
    def MergeCols(self):
        print("-------------------Merge Columns --------------------------")
        #sheet.merge_cells(start_row=1, start_column=1, end_row=sheet.max_row, end_column=2)
        for row in range(1,sheet.max_row):
            # The tibetan words and definitions are separated by Chinese symbol "："
            sheet[row][0].value = str(sheet[row][0].value) + "：" + str(sheet[row][1].value)
        sheet.delete_cols(2)
        output.save('output_dic4_corpus.xlsx')

    # Bilingual Dictionary, output files for aligment pipeline
    def ProcessDictionary(self):
        
        sheet.insert_cols(0,1)
        for row in range(1,sheet.max_row):
            Chinese_words=""
            Count = 0
            # Chinese_wordsgroup = []
            for symbol in str(sheet[row][3].value):
                if Count == 0:
                    if symbol == "：":
                        # Chinese_wordsgroup.append(Chinese_words)
                        sheet[row][0].value = Chinese_words
                        Chinese_words= ""
                        Count = 1
                    elif symbol == "。":
                        # Chinese_wordsgroup.append(Chinese_words)
                        sheet[row][0].value = Chinese_words
                        Chinese_words = ""
                        Count = 1 
                    else:
                        Chinese_words += symbol

            
        
        # for row in range(2,sheet.max_row):
            
        output.save('output_dic4_dictionary.xlsx')


    
    def ProcessSheet(self,DictionaryPath):
        self.get_execel_file(DictionaryPath)
        RowLimit = sheet.max_row
        for row in range(1,RowLimit):
            # ----------------- (1) copy Tibetan word-----------------------#
            if sheet[row][0].value is None:
                sheet[row][0].value = sheet[row-1][0].value 
            for col in range(0, sheet.max_column):
                print(f"---------------------------------Row:{row} Col:{col}------------------------------------")
                 # ------------------ (2) delete words in the brackets -----------#
                string = str(sheet[row][col].value)
                if ('(' in string) or ('（' in string) :
                    print(string)
                    p1 = re.compile(r'[(（](.*?)[)）]', re.S)
                    r1 = re.findall(p1, string)
                    print(f"Match Results: {r1}")
                    # Delete Chinese strings in the brackets 
                    new_string = string
                    for i in r1:
                        new_string = re.sub(r"[（(](.*?)[)）]","",new_string)           
                    sheet[row][col].value = new_string
                    print(f"-------Results: {sheet[row][col].value}----")
        Answer = str(input("Choose Output, (1) Corpus (2) Dictionary, Please answer 1 or 2: "))
        if Answer == "1":
            self.MergeCols()
        elif Answer =="2":
            self.ProcessDictionary()
        else:
            print("Wrong Input. Program close.")

    



class Dictionary5:

    def __init__(self):
        global ROOTDIR 
        ROOTDIR = os.getcwd()
        print(ROOTDIR)
    
    def get_execel_file(self,DictionaryPath):
        global sheet, output
        # /Dictionary/05-藏漢大詞典.xlsx
        #files = ROOTDIR +  str(DictionaryPath)
        files = ROOTDIR +  "/Dictionary/05-藏漢大詞典.xlsx"
        data = pd.ExcelFile(files)
        ps = openpyxl.load_workbook(files)
        ps.save('output_dic5.xlsx')
        output = openpyxl.load_workbook('output_dic5.xlsx')
        sheet = output[data.sheet_names[0]]
    
    def ProcessSheet(self,DictionaryPath):
        self.get_execel_file(DictionaryPath)
        RowLimit = sheet.max_row
        for row in range(1,RowLimit):
            # ----------------- (1) copy Tibetan word-----------------------#
            if sheet[row][0].value is None:
                sheet[row][0].value = sheet[row-1][0].value 
            for col in range(0, sheet.max_column):
                print(f"---------------------------------Row:{row} Col:{col}------------------------------------")
                 # ------------------ (2) delete words in the brackets -----------#
                string = str(sheet[row][col].value)
                if ('(' in string) or ('（' in string) :
                    print(string)
                    p1 = re.compile(r'[(（](.*?)[)）]', re.S)
                    r1 = re.findall(p1, string)
                    print(f"Match Results: {r1}")
                    # Delete Chinese strings in the brackets 
                    new_string = string
                    for i in r1:
                        new_string = re.sub(r"[（(](.*?)[)）]","",new_string)           
                    sheet[row][col].value = new_string
                    print(f"-------Results: {sheet[row][col].value}----")

        output.save('output_dic5.xlsx')

        


if __name__ == '__main__':
    # Dic1 = Dictionary1()
    # DicPath = str(input("Enter Dictionary File Path: "))
    # Dic1.ProcessSheet(DicPath)
    # Dic2 = Dictionary2()
    # DicPath = str(input("Enter Dictionary File Path: "))
    # Dic2.ProcessSheet(DicPath)
    # Dic3 = Dictionary3()
    # DicPath = str(input("Enter Dictionary File Path: "))
    # Dic3.ProcessSheet(DicPath)
    Dic4 = Dictionary4()
    DicPath = str(input("Enter Dictionary File Path: "))
    Dic4.ProcessSheet(DicPath)
    # Dic5 = Dictionary5()
    # DicPath = str(input("Enter Dictionary File Path: "))
    # Dic5.ProcessSheet(DicPath)