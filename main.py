# Current Implementation:
# pip install more-itertools

# Alternate Methods:
# python.exe -m pip install --upgrade pip
# python3 -m pip install more_itertools

import re
from more_itertools import powerset

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

def main():
    powerSet = []
    companyQuantity = 4
    createPowerSet(powerSet, companyQuantity)

    # DEBUG
    print("Parsed powerSet to be used for calculations:")
    print(powerSet)
    print("\n\n")
    for i in range(len(powerSet)):
        print(powerSet[i])

if __name__ == "__main__":
    main()