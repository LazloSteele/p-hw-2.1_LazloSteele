# Integer Conversionatron X

This project is a minimal TUI application intended to fulfill a class assignment for PPCC CSC2025-2H1. This assignment
is to create a program in any high level language to convert integers of the decimal, hexadecimal, or binary variety to 
any of the other types mentioned. The app uses the python standard library and handles all conversions manually.


## Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/downloads/release/python-3110/) (>= 3.11.x)

## Getting Started

### 1. Clone the Repository
The text based app is stored on the TUI branch. So be sure to clone with the -b flag 
for branch and the branch name as TUI. The cd command will move directory to the 
repository.

```console
~$ git clone -b TUI https://github.com/lazlosteele/p-hw-2.1_LazloSteele.git
~$ cd P-HW-#2.1_Lazlo-Steele
```
### 2. Initialize your Virtual Environment
This will ensure that this app will run on a clean version of python without a 
potentially polluted namespace or other issues. Enter the following command in your
terminal to initialize a virtual environment.

```console
~$ python3.11 -m venv venv
```

### 3. Activate your Virtual Environment
Depending on your OS enter one of the following commands in your terminal. Ensure that
you varify your python version with the second command in each option.

#### macOS/Linux
```console
~$ source myenv/bin/activate
~$ python --version
```

#### Windows
```console
~$ .\myenv\Scripts\activate
~$ python --version
```

### 4. Run the Application

```console
~$ cd app
~$ python main.py
```

## Using the App

### 1. Startup
Upon launching the app the full screen of your terminal should be taken by the app. A
welcome banner should display and a footer section should display all currently
acceptable commands. Though some input data validation is handled, be sure to input
single letter commands and comply with requested data types.

### 2. Your First Conversion
Using the example of the entry D for decimal, the top portion of the window will
display "DECIMAL MODE" to signify which type of data will be converted. The command
footer will instruct you to enter a decimal integer.

#### PLEASE NOTE
This app will only accept up to 16 bit binary and 32 bit hexadecimal values.

## Project Structure

```bash
.
├── .idea                
│   └── STUFF              # Directory of IDE specific items, ignore
├── app
│   ├── controllers
│   │   ├── __init__.py    # Makes the directory a python package
│   │   └── tui.py         # command flow for the TUI
│   ├── conversions
│   │   ├── __init__.py    # Makes the directory a python package
│   │   ├── binary.py      # Used for conversions from Binary
│   │   ├── conversion.py  # Parent class of the other modules in this package
│   │   ├── decimal.py     # Used for conversions from Decimal
│   │   └── hexadecimal.py # Used for conversions from Hexadecimal
│   ├── __init__.py        # Makes the directory a python package
│   ├── main.py            # Main entry point for the app
├── venv                   # Python virtual environment, ignore 
│   └── STUFF                
├── .gitignore             # Excludes files from Git Repository
├── LICENSE.md             # Project open source license
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

```