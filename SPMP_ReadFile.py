# Current Implementation:
# pip install more-itertools

import os.path

import SPMP_SETTINGS
from pathlib import Path

class Data():
    def __init__(self, quantityStockPairs, stockPairs, budget):
        self._quantityStockPairs = int(quantityStockPairs)
        self._budget = int(budget)
        self._stockPairs = [] # list of tuples, as [price, value]

        # "Sequence Unpacking" for the tuple of variable length for stock-pairs
        if stockPairs.startswith("[]"): # edge case: []
            self._stockPairs.append((0, 0))
        else:
            _sp = stockPairs.split(", ")
            _tuple = tuple(int(i.replace("[", "").replace("]", "").strip()) for i in _sp)
            _price = 0
            _value = 0
            for index, _number in enumerate(_tuple):
                if index % 2 == 0:
                    _price = _number
                else:
                    _value = _number
                    self._stockPairs.append((_price, _value))

    @property
    def quantityStockPairs(self):
        return self._quantityStockPairs

    @property
    def stockPairs(self):
        return self._stockPairs

    @property
    def budget(self):
        return self._budget


def readFile(dataCase):
    path = Path(__file__).parent.absolute()
    path = os.path.join(path, SPMP_SETTINGS.inputFileName)

    _linecount = 1
    with open(path, "r") as file:
        for line in file:
            if len(line) == 0:
                continue
            elif _linecount == 1:
                quantityStockPairs = line
            elif _linecount == 2:
                stockPairs = line
            elif _linecount == 3:
                budget = line

            _linecount += 1
            if _linecount >= 4:
                # Calculations
                _datum = Data(quantityStockPairs, stockPairs, budget)
                dataCase.append(_datum)
                # Reset Line Counter
                _linecount = 1

def isFileExist() -> bool:
    path = Path(__file__).parent.absolute()
    path = os.path.join(path, SPMP_SETTINGS.inputFileName)
    return os.path.isfile(path)