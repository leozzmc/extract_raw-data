from re import I
import openpyxl
import os
import pandas as pd 


files = []
RootDIR = os.getcwd()
os.chdir("tm-master/tm-master/sources/T12")
outputPath = RootDIR + "/output/"
outputName = "vol"

for i in range(1,33):
    files.append(f"八千頌般若經藏漢對照第{i}品.xlsx")

# length in the range() function is determine by the number of volumes you want to output
for i in range(0,len(files)):
    data = pd.ExcelFile(files[i])
    ps = openpyxl.load_workbook(files[i])
    # select sheets in excel files
    sheet = ps[data.sheet_names[0]]
    # Check if the output dir. is already exist
    isExists = os.path.exists(outputPath+outputName+str(i+1))
    # print(sheet.max_row)

    if not isExists:
        # Make Directories for each volumes
        OUPUT_DIRNAME=outputPath+outputName+str(i+1)
        os.makedirs(OUPUT_DIRNAME)
        # Output files
        with open(f"{OUPUT_DIRNAME}/{outputName}{i+1}.txt", 'w', encoding='utf16') as f:
            # Iterate rows in the sheet
            for row in range(2, sheet.max_row + 1):

                # Exceptions for vol 30~32, there are missing chinese translation in the column C in these files.
                if i > 28:
                     # ignore the None type table
                    if sheet['B' + str(row)].value is not None:
                        # Get one of Chinese tranlation of each row in the sheet
                        sutras_row = sheet['B' + str(row)].value
                        f.write(sutras_row +"\r\n")
                else:
                    # ignore the None type table
                    if sheet['C' + str(row)].value is not None:
                        # Get one of Chinese tranlation of each row in the sheet
                        sutras_row = sheet['C' + str(row)].value
                        f.write(sutras_row +"\r\n")
                    




    # Test Output
    # for row in range(2, sheet.max_row + 1):
    #             if sheet['C' + str(row)].value is not None:
    #                 sutras_row = sheet['C' + str(row)].value
    #                 print(f"-[Vol: {i+1}][Row: {row}]---------------------------------------------------------")
    #                 print(sutras_row)

    


            
   


    
    


