from pathlib import Path
from openpecha.formatters import HFMLFormatter
import os


ROOTDIR= os.getcwd()

# hfml_fn = Path("tests") / "formatters" / "hfml" / "data" / "kangyur_01.txt"
hfml_fn = Path(ROOTDIR+"/output/T12/vol1")
formatter = HFMLFormatter(output_path="opf/t12")
formatter.create_opf(hfml_fn)

