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

## Usage

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

