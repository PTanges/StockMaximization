# Current Implementation:
# pip install more-itertools

# The Stock Price Maximization Problem
# we are solving is a re-skin of the knapsack problem where budget = W (capacity) of knapsack

import SPMP_ReadFile
import SPMP_DEBUGGER_TOOL
import SPMP_SETTINGS

import SPMP_ExhaustiveApproach

def main():
    if SPMP_SETTINGS.allowFailsafe:
        if SPMP_ReadFile.isFileExist() is False:
            print(f'Unable to find {SPMP_SETTINGS.inputFileName} in local folder.')
            print("Randomly generating new stocks...")
            SPMP_DEBUGGER_TOOL.generateRandomStock()

    SPMP_ExhaustiveApproach.exhaustive_method()

    '''
    exhaustive_method()
    - generate combinations
    dynamic_method()

    both will need ReadFile, perhaps used in different ways
    - may be best that ReadFile stores all inputs from the file...
    - the array issue may be fixed with array[i].append for 2d-array[][]
    '''


if __name__ == "__main__":
    main()
