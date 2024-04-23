# Ur.PET - Your Personal Expense Tracking Program
## General Info
Inspired by James Clear's book Atomic Habit, I created a Python program called Ur.PET. It is a simple Python program for tracking personal expenses. It realizes the value of building atomic habits by empowering users to set spending targets for the day and carefully record their transactions accordingly. Ultimately, users will receive a summary or notification indicating whether their spending exceeded the target or if they managed to save money. This fosters mindful spending habits and financial awareness, thereby contributing to long-term financial well-being.
Don't miss out – visit our article on my Medium to add more perspective [here](https://medium.com/@ammarmuzacky)! or you may visit my Portfolio below:
- Exploring Efficiency: Navigating Expense Tracking with Iterable Functions [here](https://medium.com/@ammarmuzacky/d43bbb3d5445)
- Optimizing Data Handling: Enhancing Python’s CSV Export and Import Capabilities through Expense Tracking [here](https://medium.com/@ammarmuzacky/optimizing-data-handling-enhancing-pythons-csv-export-and-import-capabilities-through-expense-35e489c8015a)

### Features
1. Login: Users can log in with their username and password. (For demonstration purposes, a dummy user authentication system is implemented.)
2. Set Target Expense: Users can set their target expense for the day.
3. Add Transaction: Users can add new transactions, including date, category, amount, and details.
4. Remove Transaction: Users can remove transactions by providing the ID of the transaction.
5. Update Transaction: Users can update existing transactions by providing the ID of the transaction.
6. Summarize Expenses: Users can view a summary of their expenses for the day, including the total expense and remaining target expense.
7. View Transaction History: Users can view their transaction history, including date, category, amount, and details.
8. Reset Transaction History: Users can reset all transaction history.

### Usage
Upon running the program, you will be prompted to log in. Use the provided dummy credentials or modify the valid_credentials dictionary in the code to suit your needs.
Once logged in, you will be presented with a menu where you can choose various options to manage your expenses. After adding or updating transactions, the program will save the transaction data to a CSV file named "transaction_history.csv" in the same directory as the script. This file will contain details of all recorded transactions for future reference.


### Dependencies and Environment requirements:
1. The code is written in Python, so it requires a Python interpreter to run. The code seems compatible with Python 3.12.
2. [tabulate](https://pypi.org/project/tabulate/): A Python library for formatting tabular data.
3. CSV : Python's built-in CSV module for reading and writing CSV files.

### How to Run
1. Clone the repository:
```
git clone https://github.com/Zacky182/Python-M1-Ur.Pet.git
```
2. Install dependencies :
```
pip install tabulate
```
3. Run the application:
```
python ur_pet_v2.py
```

### Contributing
Contributions are welcome! Please feel free to open a pull request, sent to my email _ammarmuzacky@gmail.com_ or submit an issue if you encounter any problems or have suggestions for improvements.




