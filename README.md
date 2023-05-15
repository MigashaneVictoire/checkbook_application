# Python Checkbook Application

This Python application enables users to conduct a range of transactional activities on their digital checkbook. Users can check their account balances, record debits (withdrawals), record credits (deposits), and exit the program.

## Dependencies
This application was built using Python 3.8.5.

## Setup
* Save the python code to your preferred directory with an appropriate file name.
* Ensure you have Python installed on your computer.

## Usage
* Navigate to the directory where the Python code was saved and run the code.
* The user will be presented with a menu that includes the following options:
    * View current balance
    * Record a debit (withdraw)
    * Record a credit (deposit)
    * Exit
* After selecting an option, the user will be prompted to enter an amount (in dollars and cents) and confirm the transaction.
* If the user selects option 1, their current balance will be displayed. They will then be asked if they wish to continue using the program.
* If the user selects option 2, they will be asked to enter a withdrawal amount. If the amount is greater than the current balance, they will be asked to enter a different amount. The balance will be updated with the withdrawn amount.
* If the user selects option 3, they will be asked to enter a deposit amount. The balance will be updated with the deposited amount.
* If the user selects option 4, the program will exit.

## Future Updates
* Adding data persistence, for example, by writing data to a CSV file to enable users to retrieve their transaction history.
* Adding user authentication and encryption features to secure user data.