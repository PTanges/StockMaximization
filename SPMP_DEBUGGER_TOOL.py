import random
import SPMP_SETTINGS

_defaultSampleSize = 10  # Quantity of test cases to be generated, must be int(n) > 0
# Below: bounded range for stock-pair generation [min,max], must be int(n) > 0
_minStockPrice = 1
_maxStockPrice = 10
_minStockValue = 1
_maxStockValue = 15
_minBudget = 5
_maxBudget = 15
# Below: bounded range for quantity of stock-pairs generated for (price, value), must be int(n) >= 0
_minStockPairs = 0
_maxStockPairs = 8


def generateRandomStock() -> None:
    with open(SPMP_SETTINGS.inputFileName, 'w') as file:
        for i in range(_defaultSampleSize):
            _quantityStockPair = _generateQuantityStockPairs()
            _stockPairs = _generateStockOutput(_quantityStockPair)
            file.write(f'{_quantityStockPair}\n')
            file.write(f'{_stockPairs}\n')
            file.write(f'{random.randint(_minBudget, _maxBudget)}\n')
        # end for
    # end with open


def _generateStockOutput(_quantityStockPair) -> str:
    _line = "["
    for j in range(_quantityStockPair):
        if _quantityStockPair > 1:  # Formatting
            _line += "["
        _line += _generateStockPair()
        if _quantityStockPair > 1:  # Formatting
            _line += "]"
        if j < _quantityStockPair-1:  # Formatting
            _line += ", "
    _line += "]"
    return _line


def _generateStockPair() -> str:
    _line = str(random.randint(_minStockPrice, _maxStockPrice))
    _line += ", "
    _line += str(random.randint(_minStockValue, _maxStockValue))
    return _line


def _generateQuantityStockPairs() -> int:
    return random.randint(_minStockPairs, _maxStockPairs)
