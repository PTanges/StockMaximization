<div align="center">

# Stock Maximization

Stock Maximization Problem solved through Exhaustive Pattern and Dynamic Pattern.

</div>

## Installation
```sh
pip install more-itertools
```
(or)
```sh
pip3 install more-itertools
```

## Disclaimer
There may be instances where the program may not work correctly. Upon encountering such error, you may create a local virtual environment and pip install within the env. Activate the env when running the program.

```sh
python3 -m venv envStockMaximization
```

## Usage Example
Run main.py on the terminal or through an IDE after installing the necessary module(s).

Additionally, a built-in debugging assistance tool may be run. In the debugger tool file, toggle-able booleans may be used to define scope. To adjust input and output file names, refer to the settings file.

User may generate a new input file, overwrite any existing input file, quantity of test cases, and the min-max values per each parameter. Specifications for each parameter are listed within the debugger tool file. These may assist in creating test cases.
```sh
python3 SPMP_debug.py
```

Otherwise, run the code as normal.
```sh
python3 main.py
```

### Sample Input
Trailing white spaces and empty lines within an input file are permitted. Valid entry of zero available stocks should be written as "[]." Every "a" in the value-pairs (a, b) must be unique. The formatting is as follows:
> 8
>
> [[10, 13], [6, 3], [3, 5], [9, 3]]
>
> 11
>
> 0
>
> []
>
> 2
>
### Sample Output
> 13
>
> 0
>

## Sample Debugger Commands
Commands are as follows.

### Initialize debugger
```commandline
python3 SPMP_debug.py
```

### Configure Generation Parameters
Using the set command, user may alter the parameters of cases, price, value, budget, pairs, or ALL. Commands are case-sensitive.
```sh
set ALL
```

### set ALL
The user will need to enter nine integers >= 0 in corresponding order to these values. Be aware that these effects do not take effect until the user generates a new dbg.txt file.

NumberOfCases MinStockPrice MaxStockPrice MinStockValue MaxStockValue MinBudget MaxBudget MinQSP MaxQSP

Number of cases refers to how many "blocks" or cases are generated with the following threshholds.

Price refers to the weight capacity of a stock in relation to the budget.

Stock Value refers to the monetary value of the stock. This is paired with price as (price, value).

Budget refers to the maximum capacity of prices that may be bought.

QSP refers to a range of Quantity of Stock Pairs which are how many (price, value) pairs are generated per case.
```sh
20 1 30 1 10 5 10 0 6
```

### set cases
The set cases command will take one argument. Value must be >= 0, but should be >= 1 for any calculations to be done.
```commandline
set cases

1
```

### set budget
Instead of setting every value with the "ALL" command, the user may manually adjust certain ranges. The values of price, value, budget, and pairs are all ranges of [a, b] where b must be >= a and both are int >= 0. The following commands follow the same structure, taking in two arguments separated by whitespace.

"price", "value", "budget", "pairs"
```commandline
set budget

2 20

set pairs
3 6
```

### Generate dbg.txt file
```commandline
gen
```

### run command in SPMP_debug.py
To run calculations, enter any command as shown. Main will read from inputFileName.txt, generating OutputFileName-EP.txt and OutputFileName-DP.txt respectively. The input-file must be in the same folder as main.py and correspond to the name in SPMP_SETTINGS.py. The command "run main" will not read from the "_dbg.txt" generated input file.
```commandline
run main
```

### debug commands for running calculations
The generated file will only be read by the respective DBG commands shown. The output file names will be appended with "_dbg.txt" that are calculated. The "run ALL-DBG" command will run the dbg versions of the EP (Exhaustive pattern) and DP (Dynamic Pattern) respectively and output the corresponding time that calculations took to process.
```commandline
run EP-DBG

run DP-DBG

run ALL-DBG
```

### quit
The commands "quit" or "exit" will exit and close the program.
```sh
quit

exit
```

## Metadata
P. Tang - pattontanges@csu.fullerton.edu
[https://github.com/PTanges/StockMaximization/]

Submitted to Professor Dsouza as per California State University, Fullerton's Bachelor of Science, Computer Science undergraduate program.

Course: CPSC 335. Section 02.

Deadline of submission: 12/03/2023 via Canvas in a zipped folder.