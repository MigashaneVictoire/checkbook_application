import os
import csv
from datetime import datetime as dt
from curses.ascii import isdigit

# Balance file name
# balance_file_name = "bonus_user_balance_file.csv"


# Functions to animate user interface
# -----------------------------------------------------------------

# Print four options for the user
def main_menu():
    print(f"\n1) View current balance \n2) Record a debit (withdraw) \n3) Record a credit (deposit) \n4) Exit\n")

# Propt the user to chose between the opetion
def invalid_input_propt():
    print("Please enter a valid input! \n-->Enter a number between 1 and 4\n")

# Exit program
def user_exit():
    return print("\nThank you for visiting, have a great day!\n")

# Check validity of user input
def user_interface():
    '''
    --> Ask user input and check validity of the input
    '''
    while True:
        main_menu()
        user_input = input("What would you like to do?\n")
        if not user_input.isdigit(): # When user enters letters
            continue
        else:
            if int(user_input) > 4:
                invalid_input_propt() # # User input not in range 4
                continue
            return int(user_input)
            
# Check conitinuation of in transactions
def continue_transaction_propt():
    '''
    user_input -> used only to verify if interface shold continue
    return -> boolean is returned
    '''

    while True:
        user_input = input("\nWould you like to continue? (yes or no)\n")
        if not user_input.isalpha(): # When user enters numbers
            continue
        else:
            if user_input not in ["yes","y","no","n"]:
                continue
            return True if user_input in ["yes","y"] else False


# Functions to retreive data from checkbook
# -----------------------------------------------------------------
# Check existance of file
def check_file_exists(balance_file_name) -> str:
    '''
    balance_file_name -> string representing the csv file to be found
    --> Will create file if file don't exist and return a list of all values at index -1
    '''
    if os.path.exists(balance_file_name):
        # Open the existing file and retreive the balance
        with open(balance_file_name, "r") as balance_file:
            balance_file_lines = balance_file.readlines()
            return balance_file_lines[-1].replace("\n","").split(",") # cleaned list of the last index element
    else:
        print(f"File {balance_file_name[-1]} not found... \nCreating file...")

        col_names = ['id','Balance', 'TransType','DateTime'] # header row describe the column
        init_data = ["0","0", "Creation",dt.now()] # initial value when file created

        # Creating a new file with a cell holding 0
        with open(balance_file_name, 'w') as balance_file:
            writer = csv.writer(balance_file)
            writer.writerow(col_names) # Insert column names
            writer.writerow(init_data) # Insert initial data

        # Open the existing file and retreive the balance
        with open(balance_file_name, "r") as balance_file:
            balance_file_lines = balance_file.readlines()

            print(f"File {balance_file_name} has been created!")
            return balance_file_lines[-1].replace("\n","").split(",")  # return a list of elements in created file

# Show current balance
def view_curr_balance(balance_file_name) -> str:
    '''
    balance_file_name -> string representing the csv file to be found
    balanceFile_lastIndex -> iniciate balance return
    return 3 separate variables belonging to balance file last index elements
    
    '''
    # Check and report to user the balance
    balanceFile_lastIndex = check_file_exists(balance_file_name) # Retreive file
    return unpack_balance_returns (balanceFile_lastIndex) # -> primary_key, balance_value, transaction_date

# deposit and withdraw funds from balance
def user_deposit_withdraw(balance_file_name, user_amount, primary_key, trans_type) -> "str, float, int":
    '''
    balance_file_name -> string representing the csv file to be found
    user_amount -> orinal cheeckbook balance (+/-) user input amount
    balance_file -> iniciate append sequence in the csv file
    '''
    dnew_data = [str(primary_key + 1), str(user_amount), str(trans_type),str(dt.now())] # Data to be added to balance sheet

    # append new data to the balance csv file
    with open(balance_file_name, 'a') as balance_file:
            writer = csv.writer(balance_file)
            writer.writerow(dnew_data) # Insert new data
            balance_file.close()

# validate mount to degits for transactions 
def validate_user_input_amount(trans_type) -> str:
    '''
    trans_type -> type of transction the user is trying to do
    user_input -> maount user transacting
    '''
    while True:
        try:
            user_input = float(input(f"\nEnter {trans_type} amount: $"))
            if user_input < 0:
                print("\nInvalid amount... Try again!")
                continue

        except:
            print("\nInvalid amount... Try again!")
            continue

        return round(user_input, 2)

# Check if user had enough funds
def withdraw_validattion(prev_balance) -> "float":
    '''
    user_amount -> input amount from user
    prev_amount -> current user balance
    return -> new current amount
    '''
    while True:
        user_amount = validate_user_input_amount("withdraw")
        if user_amount > prev_balance:
            print(f"You  withdraw amount is greater than the current balance...\nTry a different amount!")
            continue
        return (user_amount, prev_balance - user_amount) # withdraw_amount

# Extra functions for user operations
# -----------------------------------------------------------------
# Change datatypes for each value from balance file
def unpack_balance_returns (balanceFile_lastIndex) -> list:

    primary_key = int(balanceFile_lastIndex[0])
    balance_value = float(balanceFile_lastIndex[1])
    trans_type = str(balanceFile_lastIndex[2])

    # String to datetime formate 
    transaction_date = dt.strptime(balanceFile_lastIndex[3], "%Y-%m-%d %H:%M:%S.%f")
    
    return (primary_key, balance_value, trans_type, transaction_date)

def view_historical_trans(balance_file_name):
    with open(balance_file_name) as hist_data:
        file_reader = csv.reader(hist_data)
        
        for row in file_reader:
            print(row)
    return
def category_assignment():
    return
def date_time_tracking():
    return
def user_describe_trans():
    return
def modefy_past_trans():
    return