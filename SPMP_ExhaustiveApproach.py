import re
from more_itertools import powerset

'''
# You will want these
    powerSet = []
    companyQuantity = 4 # temp value, most likely will be stored in an array
    createPowerSet(powerSet, companyQuantity)
'''

def exhaustive_method():
    pass

def createPowerSet(powerSet, companyQuantity):
    _enumeration = []
    for i in range(companyQuantity):
        _enumeration.append(i+1)

    _combinations = []
    _combinations.append(list(powerset(_enumeration)))

    # DEBUG
    print("Initial Powerset from itertools module:")
    print(_combinations)
    print("\n")

    # Parse Combinations
    _text = str(_combinations[0])
    _combinations.clear()
    _combinations = _text.split("),")

    for line in _combinations:
        powerSet.append(re.findall(r'\d+', line))
# end funct