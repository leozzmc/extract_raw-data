[![break-sentence](https://github.com/leozzmc/extract_raw-data/actions/workflows/break-sentence.yml/badge.svg?branch=BreakSentence)](https://github.com/leozzmc/extract_raw-data/actions/workflows/break-sentence.yml)

# extract_raw-data
Extract raw data(Chinese sentence) from excel files then save to text files

## Remainder
- T11 folder and T4090 is stand for different sutras.

## Installation
```
git clone https://github.com/leozzmc/extract_raw-data.git
cd extract_raw-data/
pip install -r requirement.txt
```

## Usage - Extract data

```
$ python extract.py 
Usage: extract.py [OPTIONS] COMMAND [ARGS]...

Options:
  --target TEXT  Sutras name you want to extract e.g. --target T12
  --help         Show this message and exit.

Commands:
  extract  To extract data form target excel files
```

## Example


```
python extract.py --target T11 extract
```


## Output

format: `.txt`


for each rows in excel files,I pick single Chinese tranlation as output data, unless there are missing tranlation.
for the missing Chinese translation cases, the tool will pick another version of Chinese translation.

- πOutput
  - π T11
  - π T4090
     - π vol1
     - π vol2
     - π vol3
     - π vol4
     - π vol5
     - π vol6
     - π vol7
     - π vol8
     - π vol9
        - π vol9.txt


## π Format the Chinese data (ungoing)

This script is try to turn the Chinese sentence in the "T12" sutras from Kumarajiva-Project. (https://github.com/Kumarajiva-Project/tm)

By importing the HFMLImporter module from openpecha.formatter libraries, the formatter object can be create, then call the **create_opf** function.


## β οΈREMINDER
There are existed encoding problems in **get_input** function and **write_text** function in **hfml.py**.
The "encoding" parameter needs to be changed from **'utf-8'** to **'utf16'** when encoding and decoding the Chinese symbols

*hfml.py* 

![get](https://user-images.githubusercontent.com/30616512/188070844-745c595b-c69e-415d-b259-a992f6722d56.PNG)

![create](https://user-images.githubusercontent.com/30616512/188070858-fadcb525-a77a-4cba-bad1-85761b3df3b0.PNG)



### Run the script.
```
python hfml_import.py
```

### Result.
The terminal will display the message like bellow
```
[INFO] parsing Vol vol1.txt ...
[INFO] Creating layers for v001 ...
[INFO] Creating index layer for Pecha ...
```
And you will notice that the opf folder is created.

- πopf
  - π t12
     - π vol1
       - π vol1.opf
          - π base
            - π v001.txt
          - π layers
            - πv001
          - π index.yml
          - π meta.yml
          
### v001.txt
![1](https://user-images.githubusercontent.com/30616512/188070347-0538cd1f-2e1b-4e2a-836e-22d810b2e719.PNG)

### index.yml
![2](https://user-images.githubusercontent.com/30616512/188070443-8e128788-ff79-4518-beb4-595f8b9ad2f6.PNG)

### meta.yml
![3](https://user-images.githubusercontent.com/30616512/188070511-c4cb3dfc-8439-46f1-a4b2-1da3b1afb692.PNG)




