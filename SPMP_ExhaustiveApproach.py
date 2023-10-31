import re
from more_itertools import powerset

import SPMP_ReadFile
import SPMP_SETTINGS

def exhaustive_method():
    dataCase = [] # Store all data from file
    output = [] # Stores all maximum values from the cases
    SPMP_ReadFile.readFile(dataCase)
    calculateOutput(dataCase, output)
    write_output(output)

def calculateOutput(dataCase, output):
    maximums = []
    powerSet = []
    for datum in dataCase:
        createPowerSet(powerSet, datum.quantityStockPairs)
        for _combination in powerSet[1:]:
            _maxValue = 0
            _totalPrice = 0
            for _number in _combination:
                _totalPrice += datum.stockPairs[int(_number)-1][0]
                _maxValue += datum.stockPairs[int(_number)-1][1]
            maximums.append((_totalPrice, _maxValue))

        _bestValue = 0
        for i in range(len(maximums)):
            if (maximums[i][0] <= datum.budget and maximums[i][1] > _bestValue):
                _bestValue = maximums[i][1]
        output.append(_bestValue)

        maximums.clear()
        powerSet.clear()

def createPowerSet(powerSet, quantityStockPairs):
    _enumeration = []
    for i in range(quantityStockPairs):
        _enumeration.append(i+1)

    _combinations = []
    _combinations.append(list(powerset(_enumeration)))

    # Parse Combinations
    _text = str(_combinations[0])
    _combinations.clear()
    _combinations = _text.split("),")

    for line in _combinations:
        powerSet.append(re.findall(r'\d+', line))
# end funct

def write_output(bestValues):
    with open(SPMP_SETTINGS.outputFileName, 'w') as file:
        for _value in bestValues:
            file.write(f'{_value}\n')
    #end with open