import SPMP_SETTINGS
import SPMP_DEBUGGER_TOOL
import SPMP_ExhaustiveApproach
import SPMP_DynamicApproach
import time
import main

PATTERNS = ["main", "EP-DBG", "DP-DBG", "ALL-DBG"]
# To do: implement ability to alter input and output file names


def dbg_main():
    FileHandler = SPMP_DEBUGGER_TOOL.FileGenerator()
    DebugHandler = SPMP_DEBUGGER_TOOL.DebugData()
    print(f'Debugger initialized. Target File: {SPMP_SETTINGS.inputFileName.replace(".txt", "_dbg.txt")}')
    while True:
        promptUser()
        command = input(f'> ')
        print()
        _flag, args = validateCommand(command)
        if _flag == -1: continue
        elif _flag == 0: break
        elif _flag == 1: printHelp()
        elif _flag == 2: generateFile(FileHandler, DebugHandler)
        elif _flag == 3: runPattern(args)
        elif _flag == 4: setGenParameters(args, DebugHandler)
        else:
            continue
    # end while
    print("Exiting debugger.")
    quit()


def promptUser():
    print(f'Enter a command:')


def validateCommand(command):  # -> int, list[str]
    if len(command) > 40 or len(command) < 3:
        return -1, command
    PARAMETERS = SPMP_DEBUGGER_TOOL.PARAMETERS  # set DebugHandler parameters

    _command = command.strip(" ")
    try:
        _args = _command.split(" ")
        if _args[0] == ("quit" or "exit"): return 0, ""
        elif _args[0] == ("help" or "?" or "rules"): return 1, ""
        elif _args[0] == "gen": return 2, ""
        elif _args[0] == "run" and _args[1] in PATTERNS: return 3, _args[1:]
        elif _args[0] == "set" and _args[1] in PARAMETERS: return 4, _args[1:]
        else: printErrorStatement()
    except (TypeError, NameError, IndexError, SyntaxError, ValueError):
        return -1, _command

    return -1, _command


def printErrorStatement() -> None:
    print("Invalid statement. Please try again\n")


def printHelp() -> None:
    rules = "Commands are as shown.\n"
    rules += "\t> gen\n"
    rules += "\t> run EP\n"
    rules += "\t> run DP\n"
    rules += "\t> run ALL\n"
    rules += "\t> set price\n"
    rules += "\t> set value\n"
    rules += "\t> set budget\n"
    rules += "\t> set pairs\n"
    rules += "\t> set ALL\n"
    rules += "\t> set {int} {int} {int} {int} {int} {int} {int} {int}\n"
    rules += "\t> quit (or) exit\n"
    print(rules)


def getTime() -> float:
    return time.time()


def printTimeElapsed(start, end) -> None:
    print(f'Time elapsed: {end - start:.04f} seconds.\n')


def generateFile(FileHandler, DebugHandler) -> None:
    _s = getTime()
    FileHandler.generateRandomStock(DebugHandler)
    _e = getTime()
    print(f'File {SPMP_SETTINGS.inputFileName.replace(".txt", "_dbg.txt")} generated.')
    printTimeElapsed(_s, _e)


def runPattern(args) -> None:
    if args[0] not in PATTERNS:
        print("Pattern not found. Try again.\n")
        return

    local_IPFN = SPMP_SETTINGS.inputFileName.replace(".txt", "_dbg.txt")
    local_OPFN_EP = SPMP_SETTINGS.outputFileNameEP.replace(".txt", "_dbg.txt")
    local_OPFN_DP = SPMP_SETTINGS.outputFileNameDP.replace(".txt", "_dbg.txt")
    print(f'Running {args[0]} on {SPMP_SETTINGS.inputFileName.replace(".txt", "_dbg.txt")}')

    _s = getTime()
    if args[0] == PATTERNS[0]:
        main.main()
    elif args[0] == PATTERNS[1]:
        SPMP_ExhaustiveApproach.exhaustive_method(local_IPFN, local_OPFN_EP)
    elif args[0] == PATTERNS[2]:
        SPMP_DynamicApproach.dynamic_method(local_IPFN, local_OPFN_DP)
    elif args[0] == PATTERNS[3]:
        SPMP_ExhaustiveApproach.exhaustive_method(local_IPFN, local_OPFN_EP)
        SPMP_DynamicApproach.dynamic_method(local_IPFN, local_OPFN_DP)
    _e = getTime()
    printTimeElapsed(_s, _e)


# To do: reformat to accept a quantity of parameters based on Arg
def setGenParameters(args, DebugHandler) -> None:
    if args[0] == "ALL":
        _promptGenALL = "Enter nine integer values where max >= min and all values are int >= 0.\n"
        _promptGenALL += "Numbers should be as follows:\n\t"
        _promptGenALL += "numOfCases minStockPrice maxStockPrice minStockValue maxStockValue minBudget maxBudget" \
                         " minQSP maxQSP\n\n\t"
        _promptGenALL += "- numOfCases refers to separate instances of data for companies, stock price values, " \
                         "& budget\n\t"
        _promptGenALL += "- QSP stands for 'quantity of stock pairs.' per case. [price, value]...\n\t"
        _promptGenALL += "- and if generated QSP > [minStockPrice, maxStockPrice],\n\t"
        _promptGenALL += "- then QSP will be generated in the range of [minStockPrice, maxStockPrice]"
        while True:
            print(_promptGenALL)
            _command = input("> ")
            _flag, data = _validateGenAllInput(_command)
            if _flag == -1: continue
            elif _flag == 0:
                _setAllDebugParameters(data, DebugHandler)
                print("Values set!\n\n")
                print(DebugHandler)
                break
    elif args[0] == "cases":
        while True:
            print("Enter an integer >= 0 for quantity of cases.")
            _command = input("> ")
            try:
                _command = int(_command)
                if _command >= 0:
                    DebugHandler.set_sampleSize(_command)
                    print(f'Quantity of cases set to: {DebugHandler.sampleSize}.\n')
                    break
            except (TypeError, NameError, IndexError, SyntaxError, ValueError):
                "Invalid input. Try again.\n"
    elif args[0] in SPMP_DEBUGGER_TOOL.PARAMETERS:
        # "price", "value", "budget", "pairs"
        # _setDebugParameters(parameters, DebugHandler, args[0])
        _promptGenParams = "Enter number(s) where max > min and both are int >= 0."
        while True:
            print(_promptGenParams)
            _command = input("> ")
            _flag, data = _validateGenParamInput(_command)
            if _flag == -1: continue
            elif _flag == 0:
                _setDebugParameters(data, DebugHandler, args[0])
                print("Values set!")
                print(f'{args[0]}: [{data[0]},{data[1]}].\n')
                break


def _validateGenAllInput(args):  # -> int, list[int]
    _error = "Invalid amount or value-types given.\nInput nine integer values of min <= max and both <= 0.\n"
    result = []
    try:
        _args = args.strip(" ").split(" ")
        if len(_args) != 9:
            print(_error)
            return -1, result

        for arg in _args:
            if type(arg) == float or int(arg) < 0:
                print(_error)
                return -1, result

        for i in _args:
            result.append(int(i))

        # Max > Min, index 0 is skipped
        for i in range(len(result)-1)[1:]:
            if i % 2 == 0:
                if result[i] <= result[i+1]:
                    print(_error)
                    return -1, result

        # Set pairs to 0 if cases = 0
        if result[0] == 0:
            result[-1] = 0
            result[-2] = 0

        return 0, result
        # return _args

    except (TypeError, NameError, IndexError, SyntaxError, ValueError):
        return -1, result


def _validateGenParamInput(args):
    _error = "Numbers must be integers >= 0. Max must be > min."
    result = []
    try:
        _args = args.strip(" ").split(" ")
        if len(_args) != 2:
            print(_error)
            return -1, result

        for arg in _args:
            if type(arg) == float or int(arg) < 0:
                print(_error)
                return -1, result

        for i in _args:
            result.append(int(i))

        # Max > Min, index 0 is skipped
        if result[0] > result[1]:
            print(_error)
            return -1, result
        return 0, result
    except (TypeError, NameError, IndexError, SyntaxError, ValueError):
        return -1, result


def _setAllDebugParameters(parameters, DebugHandler) -> None:
    DebugHandler.set_sampleSize(parameters[0])
    DebugHandler.set_stockPrices(parameters[1], parameters[2])
    DebugHandler.set_stockValueRange(parameters[3], parameters[4])
    DebugHandler.set_budgetRange(parameters[5], parameters[6])
    DebugHandler.set_stockPairRange(parameters[7], parameters[8])
    return


def _setDebugParameters(parameters, DebugHandler, args) -> None:
    _pairName = args[0]
    # "cases", "price", "value", "budget", "pairs"
    if _pairName == "price":
        DebugHandler.set_stockPrices(parameters[0], parameters[1])
    elif _pairName == "value":
        DebugHandler.set_stockValueRange(parameters[0], parameters[1])
    elif _pairName == "budget":
        DebugHandler.set_budgetRange(parameters[0], parameters[1])
    elif _pairName == "pairs":
        DebugHandler.set_stockPairRange(parameters[0], parameters[1])
    return


if __name__ == "__main__":
    dbg_main()
