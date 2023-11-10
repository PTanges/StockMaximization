import re
from more_itertools import powerset

import SPMP_ReadFile
import SPMP_SETTINGS


def exhaustive_method() -> None:
    dataCase = SPMP_ReadFile.readFile(SPMP_ReadFile.getFilepath())
    maximumValues = calculateOutput(dataCase)
    write_output(maximumValues)


def calculateOutput(dataCase) -> list[int]:
    output = []
    for datum in dataCase:
        _populateOutput(datum, output)
    return output


def _populateOutput(datum, output) -> None:
    powerSet = createPowerSet(datum.quantityStockPairs)
    maximums = generateMaxValue(powerSet, datum)
    parseValidMaximums(maximums, datum.budget, output)


def generateMaxValue(powerSet, datum) -> list[tuple[int, int]]:
    maximums = []
    for _combination in powerSet[1:]:
        _totalPrice = 0
        _maxValue = 0
        for _number in _combination:
            _totalPrice += datum.stockPairs[int(_number)-1][0]
            _maxValue += datum.stockPairs[int(_number)-1][1]
        maximums.append((_totalPrice, _maxValue))
    return maximums


def parseValidMaximums(maximums, budget, output) -> None:
    _bestValue = 0
    for i in range(len(maximums)):
        if maximums[i][0] <= budget and maximums[i][1] > _bestValue:
            _bestValue = maximums[i][1]
    output.append(_bestValue)


def createPowerSet(quantityStockPairs) -> list[list]:
    powerSet = []
    _enumeration = []
    for i in range(quantityStockPairs):
        _enumeration.append(i+1)

    _combinations = list(powerset(_enumeration))

    # Parse Combinations
    _text = str(_combinations[0])
    _combinations.clear()
    _combinations = _text.split("),")

    for line in _combinations:
        powerSet.append(re.findall(r'\d+', line))
    return powerSet
# end funct


def write_output(bestValues) -> None:
    with open(SPMP_SETTINGS.outputFileName, 'w') as file:
        for _value in bestValues:
            file.write(f'{_value}\n')
    # end with open
    
