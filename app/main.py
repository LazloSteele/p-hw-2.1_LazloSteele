"""
Conversionatron X: a program to convert decimal to binary and hex, and any which other way

Programmer: Lazlo F. Steele
Course: CSC2025 2H1 - Computer Architecture and Assembly Language
Date: Sept. 5, 2024
Language: Python 3.11

The main module is an entry point which loads the TUI application. The TUI handles user I/O
and manages the application state and the command flow. All the conversion modules are called
by TUI.py and are held in the conversions package.

"""

from controllers.tui import TUI

app = TUI()
