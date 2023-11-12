import os.path
import SPMP_SETTINGS
from pathlib import Path


class Data:
    def __init__(self, quantityStockPairs, stockPairs, budget):
        self._quantityStockPairs = int(quantityStockPairs)
        self._budget = int(budget)
        self._stockPairs = parseAndPopulateTuple(stockPairs)

    @property
    def quantityStockPairs(self):
        return self._quantityStockPairs

    @property
    def stockPairs(self):
        return self._stockPairs

    @property
    def budget(self):
        return self._budget


def readFile(path) -> list[Data]:
    dataCase = []
    _populateDataCase(dataCase, path)
    return dataCase


def _populateDataCase(dataCase, path) -> None:
    _linecount = 1
    with open(path, "r") as file:
        for line in file:
            if len(line) == 0: continue
            elif _linecount == 1: quantityStockPairs = line
            elif _linecount == 2: stockPairs = line
            elif _linecount == 3:
                budget = line
                _datum = Data(quantityStockPairs, stockPairs, budget)
                dataCase.append(_datum)
                _linecount = 0
            _linecount += 1


def isFileExist(path) -> bool:
    return os.path.isfile(path)


# "Sequence Unpacking" for the tuple of variable length for stock-pairs
def parseAndPopulateTuple(stockPairs) -> list[tuple[int, int]]:
    _stockPairs = []

    # Edge Case with 0 generated stock pairs leaves [] as input
    if stockPairs.startswith("[]"):
        _stockPairs.append((0, 0))
        return _stockPairs

    _sp = stockPairs.split(", ")
    _tuple = tuple(int(i.replace("[", "").replace("]", "").strip()) for i in _sp)
    _price = 0
    _value = 0
    for index, _number in enumerate(_tuple):
        if index % 2 == 0:
            _price = _number
        else:
            _value = _number
            _stockPairs.append((_price, _value))
    return _stockPairs


def getFilepath() -> str:
    path = Path(__file__).parent.absolute()
    path = os.path.join(path, SPMP_SETTINGS.inputFileName)
    return path
