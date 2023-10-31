import re
from more_itertools import powerset

import SPMP_ReadFile

def exhaustive_method():
    dataCase = [] # Store all Data from file
    powerSet = [] # Store all combinations
    output = [] # Stores all maximum values from the cases
    SPMP_ReadFile.readFile(dataCase)
    createPowerSet(powerSet, dataCase[0].quantityStockPairs)

def createPowerSet(powerSet, quantityStockPairs):
    _enumeration = []
    for i in range(quantityStockPairs):
        _enumeration.append(i+1)

    _combinations = []
    _combinations.append(list(powerset(_enumeration)))

    '''
    # DEBUG
    print("Initial Powerset from itertools module:")
    print(_combinations)
    print("\n")
    '''

    # Parse Combinations
    _text = str(_combinations[0])
    _combinations.clear()
    _combinations = _text.split("),")

    for line in _combinations:
        powerSet.append(re.findall(r'\d+', line))
# end funct