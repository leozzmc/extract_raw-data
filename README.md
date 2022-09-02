# extract_raw-data
Extract raw data from excel files then save to text files

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

- 📂Output
  - 📂 T11
  - 📂 T4090
     - 📁 vol1
     - 📁 vol2
     - 📁 vol3
     - 📁 vol4
     - 📁 vol5
     - 📁 vol6
     - 📁 vol7
     - 📁 vol8
     - 📁 vol9
        - 📄 vol9.txt


## 📑 Format the Chinese data (ungoing)

This script is try to turn the Chinese sentence in the "T12" sutras from Kumarajiva-Project. (https://github.com/Kumarajiva-Project/tm)

By importing the HFMLImporter module from openpecha.formatter libraries, the formatter object can be create, then call the **create_opf** function.


## ⚠️REMINDER
There existed encoding problem in the hfml.py **get_input** function and **write_text** function.
the "encoding" parameter needs to changed to **'utf16'** when encoding and decoding the Chinese symbols

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

- 📂opf
  - 📂 t12
     - 📁 vol1
       - 📁 vol1.opf
          - 📁 base
          - 📁 layers
          - 📑 index.yml
          - 📑 meta.yml

