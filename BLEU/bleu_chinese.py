from nltk.translate.bleu_score import *
from itertools import count
import os, re
import openpyxl
import pandas as pd



ReferenceDataPath=[
    "/../EN-Dictionary/DR詞彙解釋.xlsx",
    "/../EN-Dictionary/GP詞彙解釋.xlsx",
    "/../EN-Dictionary/HL詞彙解釋.xlsx",
    "/../EN-Dictionary/ML詞彙表.xlsx",
    "/../EN-Dictionary/MP辭彙說明.xlsx",
    "/../EN-Dictionary/T詞彙解釋.xlsx",
    "/../EN-Dictionary/TGSM引用文典對照表.xlsx",
    "/../EN-Dictionary/TGSM詞彙選列對照表.xlsx",
    "/../EN-Dictionary/二十一度母 _ 八救難母 _ 詞彙表.xlsx"
]

HypothesisDataPath=[
    "/../EN-Dictionary/Test_for_BLEU/Glossary_Counsels/sheet1/sheet1.xlsx",
    "/../EN-Dictionary/Test_for_BLEU/Glossary_Counsels/sheet2/sheet2.xlsx",
    "/../EN-Dictionary/Test_for_BLEU/Glossary_Counsels/sheet3/sheet3.xlsx",
    "/../EN-Dictionary/Test_for_BLEU/Glossary_Counsels/sheet4/sheet4.xlsx",
    "/../EN-Dictionary/Test_for_BLEU/Glossary_Counsels/sheet5/sheet5.xlsx",
    "/../EN-Dictionary/Test_for_BLEU/Glossary_Counsels/sheet6/sheet6.xlsx",
    "/../EN-Dictionary/Test_for_BLEU/Glossary_Counsels/sheet7/sheet7.xlsx",
    "/../EN-Dictionary/Test_for_BLEU/Glossary_Counsels/sheet8/sheet8.xlsx",
    "/../EN-Dictionary/Test_for_BLEU/Glossary_Counsels/sheet9/sheet9.xlsx"
]

class Excel_Data:

    def __init__(self):
        global ROOTDIR 
        ROOTDIR = os.getcwd()
        print(ROOTDIR)

    def get_execel_file(self,DataPath):
        global sheet, output
        # files = ROOTDIR +  "/../EN-Dictionary/DR詞彙解釋.xlsx"
        files = ROOTDIR +  DataPath
        data = pd.ExcelFile(files)
        ps = openpyxl.load_workbook(files)
        sheet = ps[data.sheet_names[0]]

    def ProcessSheet(self, DataPath):
        global OutputList
        OutputList= []
        self.get_execel_file(DataPath)
        for row in range(2,sheet.max_row):
            if sheet[row][0].value is not None:
                OutputList.append(str(sheet[row][0].value))
        return OutputList

class Reference:

    def __init__(self):
        global data,reference
        data = Excel_Data()
        ## List for store "Return List"
        reference = []
        for i in ReferenceDataPath:
            reference.append(data.ProcessSheet(i))

    def check_reference(self):
        for i in range(0, len(reference)):
            print(f"------------------------------Reference{i}-------------------------------")
            for j in range(0,len(reference[i])):
                print(f"row{j} : {reference[i][j]}")

class Hypothesis:

    def __init__(self):
        global ex, hypothesis
        ex = Excel_Data()
        hypothesis = []
        for i in HypothesisDataPath:
            hypothesis.append(ex.ProcessSheet(i))
    
    def check_hypothesis(self):
        for i in range(0, len(hypothesis)):
            print(f"------------------------------Hypothesis{i}-------------------------------")
            for j in range(0,len(hypothesis[i])):
                print(f"row{j} : {hypothesis[i][j]}")



if __name__ == '__main__':
    ## initialize Reference and Hypothesis objects
    ref = Reference()
    hyp = Hypothesis()
    smo = SmoothingFunction()
    print(sentence_bleu([reference[0], reference[1], reference[2], reference[3], reference[4], reference[5]],reference[6], smoothing_function=smo.method1))

    
