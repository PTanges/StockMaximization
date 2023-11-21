import random
import SPMP_SETTINGS

defaultSampleSize = 10  # Quantity of test cases to be generated, must be int(n) > 0

# Bounded range for stock-pair generation [min,max], must be int(n) > 0. Max must be >= min.
defaultMinStockPrice = 1
defaultMaxStockPrice = 10
defaultMinStockValue = 1
defaultMaxStockValue = 15
defaultMinBudget = 5
defaultMaxBudget = 15

# Bounded range for quantity of stock-pairs generated for [price, value], must be int(n) >= 0. Max must be >= min.
defaultMinStockPairs = 0
defaultMaxStockPairs = 8

PARAMETERS = ["cases", "price", "value", "budget", "pairs", "ALL"]

class DebugData:
    def __init__(self):
        self._sampleSize = defaultSampleSize
        self._minStockPrice = defaultMinStockPrice
        self._maxStockPrice = defaultMaxStockPrice
        self._minStockValue = defaultMinStockValue
        self._maxStockValue = defaultMaxStockValue
        self._minBudget = defaultMinBudget
        self._maxBudget = defaultMaxBudget
        self._minStockPairs = defaultMinStockPairs
        self._maxStockPairs = defaultMaxStockPairs

    @property
    def sampleSize(self) -> int:
        return self._sampleSize

    def set_sampleSize(self, new):
        if new >= 0:
            self._sampleSize = new

    @property
    def minStockPrice(self) -> int:
        return self._minStockPrice

    @property
    def maxStockPrice(self) -> int:
        return self._maxStockPrice

    def set_stockPrices(self, _min, _max):
        if _max >= _min >= 0 and _max >= 0:
            self._minStockPrice = _min
            self._maxStockPrice = _max

    @property
    def minStockValue(self) -> int:
        return self._minStockValue

    @property
    def maxStockValue(self) -> int:
        return self._maxStockValue

    def set_stockValueRange(self, _min, _max):
        if _max >= _min >= 0 and _max >= 0:
            self._minStockValue = _min
            self._maxStockValue = _max

    @property
    def minBudget(self) -> int:
        return self._minBudget

    @property
    def maxBudget(self) -> int:
        return self._maxBudget

    def set_budgetRange(self, _min, _max):
        if _max >= _min >= 0 and _max >= 0:
            self._minBudget = _min
            self._maxBudget = _max

    @property
    def minStockPairs(self) -> int:
        return self._minStockPairs

    @property
    def maxStockPairs(self) -> int:
        return self._maxStockPairs

    def set_stockPairRange(self, _min, _max):
        if _max >= _min >= 0 and _max >= 0:
            self._minStockPairs = _min
            self._maxStockPairs = _max

    def __str__(self) -> str:
        result = ""
        result += "Quantity of Cases: " + str(self._sampleSize) + "\n"
        result += "Minimum stock price: " + str(self._minStockPrice) + "\n"
        result += "Maximum stock price: " + str(self._maxStockPrice) + "\n"
        result += "Minimum stock value: " + str(self._minStockValue) + "\n"
        result += "Maximum stock value: " + str(self._maxStockValue) + "\n"
        result += "Minimum budget/capacity: " + str(self._minBudget) + "\n"
        result += "Maximum budget/capacity: " + str(self._maxBudget) + "\n"
        result += "Minimum amount of pairs: " + str(self._minStockPairs) + "\n"
        result += "Maximum amount of pairs: " + str(self._maxStockPairs) + "\n"
        return result


class FileGenerator:
    def __init__(self):
        pass

    def generateRandomStock(self, _DbgData) -> None:
        localFileName = SPMP_SETTINGS.inputFileName
        localFileName = localFileName.replace(".txt", "_dbg.txt")
        with open(localFileName, 'w') as file:
            for i in range(_DbgData.sampleSize):
                _quantityStockPair = self._generateQuantityStockPairs(_DbgData.minStockPairs, _DbgData.maxStockPairs)

                if _quantityStockPair > (_DbgData.maxStockPrice - _DbgData.minStockPrice):
                    _quantityStockPair = random.randint(_DbgData.minStockPrice, _DbgData.maxStockPrice)

                _stockPairs = self._generateStockOutput(_quantityStockPair, _DbgData.minStockPrice,
                                                        _DbgData.maxStockPrice, _DbgData.minStockValue,
                                                        _DbgData.maxStockValue)
                if _stockPairs == "[]":
                    _quantityStockPair = 0
                file.write(f'{_quantityStockPair}\n')
                file.write(f'{_stockPairs}\n')
                file.write(f'{random.randint(_DbgData.minBudget, _DbgData.maxBudget)}\n')
            # end for
        # end with open

    def _generateStockOutput(self, _quantityStockPair, minStockPrice, maxStockPrice, minStockValue,
                             maxStockValue) -> str:
        if _quantityStockPair > (maxStockPrice - minStockPrice):
            return "[]"

        # Generate unique stockPrices
        _randomPrices = random.sample(range(minStockPrice, maxStockPrice), _quantityStockPair)
        _line = "["
        for j in range(_quantityStockPair):
            if _quantityStockPair > 1:  # Formatting
                _line += "["
            _line += self._generateStockPair(_randomPrices, j, minStockValue, maxStockValue)
            if _quantityStockPair > 1:  # Formatting
                _line += "]"
            if j < _quantityStockPair - 1:  # Formatting
                _line += ", "
        _line += "]"
        return _line

    @staticmethod
    def _generateStockPair(_randomPrices, j, minStockValue, maxStockValue) -> str:
        _line = str(_randomPrices[j])
        _line += ", "
        _line += str(random.randint(minStockValue, maxStockValue))
        return _line

    @staticmethod
    def _generateQuantityStockPairs(minStockPairs, maxStockPairs) -> int:
        return random.randint(minStockPairs, maxStockPairs)
