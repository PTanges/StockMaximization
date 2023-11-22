import SPMP_ReadFile


def dynamic_method(inputFileName, outputFileName) -> None:
    dataCase = SPMP_ReadFile.readFile(SPMP_ReadFile.getFilepath(inputFileName))
    output = calculateOutput(dataCase)
    write_output(output, outputFileName)


def calculateOutput(dataCase) -> list[int]:
    result = []
    for data in dataCase:
        # budget+1 = num of columns
        # quantityStockPairs+1 = num of rows
        _dataGrid = [[0] * (data.budget + 1) for _val in range(data.quantityStockPairs + 1)]
        for _currentPriceIndex in range(1, data.quantityStockPairs+1):
            for _currentBudgetValue in range(0, data.budget+1):
                if data.stockPairs[_currentPriceIndex-1][0] > _currentBudgetValue:  # price exceeds currentBudgetColumn
                    _dataGrid[_currentPriceIndex][_currentBudgetValue] = _dataGrid[_currentPriceIndex-1][_currentBudgetValue]
                else:
                    _a = _dataGrid[_currentPriceIndex-1][_currentBudgetValue]
                    _b = _dataGrid[_currentPriceIndex-1][_currentBudgetValue - data.stockPairs[_currentPriceIndex-1][0]]
                    _b += data.stockPairs[_currentPriceIndex-1][1]
                    # a = row above's value
                    # b = last value where adding current price = current budget
                    _dataGrid[_currentPriceIndex][_currentBudgetValue] = max(_a, _b)
            # end for
        # end for
        result.append(_dataGrid[-1][-1])
    # end for
    return result


def write_output(bestValues, outputFileName) -> None:
    with open(outputFileName, 'w') as file:
        for _value in bestValues:
            file.write(f'{_value}\n')
    # end with open
