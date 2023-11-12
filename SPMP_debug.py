import SPMP_ReadFile
import SPMP_DEBUGGER_TOOL
import SPMP_ExhaustiveApproach


def main():
    if checkStockFileGenerationRules():
        SPMP_DEBUGGER_TOOL.generateRandomStock()

        if SPMP_DEBUGGER_TOOL.doRunMainEP:
            SPMP_ExhaustiveApproach.exhaustive_method()

        if SPMP_DEBUGGER_TOOL.doRunMainDP:
            pass
            # SPMP_DynamicApproach.dynamic_method()

def checkStockFileGenerationRules() -> bool:
    if SPMP_DEBUGGER_TOOL.allowFailsafe:
        if SPMP_ReadFile.isFileExist(SPMP_ReadFile.getFilepath()) is False or SPMP_DEBUGGER_TOOL.allowFileOverwrite:
            return True
    return False

if __name__ == "__main__":
    main()

