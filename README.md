# extract_raw-data
Extract Raw Data from Excel

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

![image](https://user-images.githubusercontent.com/30616512/184844195-94e46607-509b-4161-a19f-d9e908ae3f08.png)
