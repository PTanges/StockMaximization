# Current Implementation:
# pip install more-itertools

import os.path

import SPMP_SETTINGS
from pathlib import Path

def isFileExist() -> bool:
    path = Path(__file__).parent.absolute()
    path = os.path.join(path, SPMP_SETTINGS.inputFileName)
    return os.path.isfile(path)