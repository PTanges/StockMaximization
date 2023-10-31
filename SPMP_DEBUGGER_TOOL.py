import random
import SPMP_SETTINGS

# Allows the program to write over either an existing inputFileName or a non-existing file
# Allows dev to continually generate the file without manual deletion
allowOverrideGeneration = False

_defaultSampleSize = 10 # Quantity of test cases to be generated, must be int(n) > 0
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

def generateRandomStock():
    with open(SPMP_SETTINGS.inputFileName, 'w') as file:
        for i in range(_defaultSampleSize):
            _quantityStockPair = random.randint(_minStockPairs, _maxStockPairs)
            file.write(f'{_quantityStockPair}\n')
            _line = "["
            for j in range(_quantityStockPair):
                if _quantityStockPair > 1: # Formatting
                    _line += "["
                _line += str(random.randint(_minStockPrice,_maxStockPrice))
                _line += ", "
                _line += str(random.randint(_minStockValue,_maxStockValue))
                if _quantityStockPair > 1: # Formatting
                    _line += "]"
                if j < _quantityStockPair-1: # Formatting
                    _line += ", "
            _line += "]"

            file.write(f'{_line}\n')
            file.write(f'{random.randint(_minBudget, _maxBudget)}\n')
        # end for
    # end with open
    print(f'{_defaultSampleSize} samples generated.')