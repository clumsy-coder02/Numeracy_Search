# Numeracy Search

A command-line tool for finding specific types of numbers within a given range.

## Description

Numeracy Search is a Python application that helps you discover various categories of numbers based on mathematical properties. Simply enter a range and choose what type of numbers you'd like to find.

## Features

- **Even Numbers**: Find all even numbers within a specified range
- **Odd Numbers**: Find all odd numbers within a specified range
- **Prime Numbers**: Identify all prime numbers within a specified range
- **Composite Numbers**: Find all composite (non-prime) numbers within a specified range

## Requirements
- Python 3.x

## Installation

1. Clone or download this repository
2. Navigate to the project directory

## Usage

Run the program from the command line:

```bash
python main.py or python3 main.py
```

### How to Use

1. The program will display a menu with 5 options:
   - Enter `1` to find **Even Numbers**
   - Enter `2` to find **Odd Numbers**
   - Enter `3` to find **Prime Numbers**
   - Enter `4` to find **Composite Numbers**
   - Enter `5` to **Exit**

2. Select your desired option
3. Enter the lowest number in your range
4. Enter the highest number in your range
5. View the results!

### Example

```bash
Command Line Numeracy Search
"Find certain numbers given a certain range"

Enter 1 for:Even Numbers
Enter 2 for:Odd Numbers
Enter 3 for:Prime Numbers
Enter 4 for:Composite Numbers
Enter 5 for:Exit

What would you like to find? 1
Finding even numbers:
Enter the lowest number: 1
Enter the highest number: 20
Even numbers between 1 & 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## Project Structure

- `main.py` - Main application file containing all the number-finding functions
- `readme.md` - This file

## Author

Created as a Python learning project

## License
Open source - feel free to use and modify
