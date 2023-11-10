# Current Implementation, include in Readme
# pip install more-itertools

# The Stock Price Maximization Problem

import SPMP_ReadFile
import SPMP_DEBUGGER_TOOL
import SPMP_SETTINGS
import SPMP_ExhaustiveApproach


def main():
    if checkStockFileGenerationRules():
        SPMP_DEBUGGER_TOOL.generateRandomStock()
    SPMP_ExhaustiveApproach.exhaustive_method()
    # SPMP_DynamicApproach.dynamic_method()


def checkStockFileGenerationRules() -> bool:
    if SPMP_SETTINGS.allowFailsafe:
        if SPMP_ReadFile.isFileExist(SPMP_ReadFile.getFilepath()) is False or SPMP_SETTINGS.allowFileOverwrite:
            return True
    return False


if __name__ == "__main__":
    main()
