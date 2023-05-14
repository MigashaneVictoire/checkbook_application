import os
import csv
from curses.ascii import isdigit

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
    --> Will create file if file don't exist and return a list of all values
    '''
    if os.path.exists(balance_file_name):
        # Open the existing file and retreive the balance
        with open(balance_file_name, "r") as balance_file:
            balance_file_lines = balance_file.readlines()
            return balance_file_lines
    else:
        print(f"File {balance_file_name} not found... \nCreating file...")

        # Creating a new file with a cell holding 0
        with open(balance_file_name, 'w') as balance_file:
            balance_file.writelines(["0"])

        # Open the existing file and retreive the balance
        with open(balance_file_name, "r") as balance_file:
            balance_file_lines = balance_file.readlines()

            print(f"File {balance_file_name} has been created!")
            return balance_file_lines  # return a list of elements in created file

# Show current balance
def view_curr_balance(balance_file_name) -> str:
    '''
    balance_file_name -> string representing the csv file to be found
    balance -> iniciate balance file
    curr_balance -> balance is returned as integer after replacing \\n
    '''
    # Check and report to user the balance
    balance = check_file_exists(balance_file_name) # Retreive file
    curr_balance = str(balance[-1]).replace('\n', "")
    return float(curr_balance)

# deposit and withdraw funds from balance
def user_deposit_withdraw(balance_file_name, user_amount) -> "str, float":
    '''
    balance_file_name -> string representing the csv file to be found
    user_amount -> orinal cheeckbook balance (+/-) user input amount
    balance_file -> iniciate append sequence in the csv file
    '''
    balance_file = csv.writer(open(balance_file_name, 'a'), dialect='excel')
    balance_file.writerow([user_amount])

# validate mount to degits for transactions 
def validate_user_input_amount(trans_type) -> str:
    '''
    trans_type -> type of transction the user is trying to do
    user_input -> maount user transacting
    '''
    while True:
        user_input = input(f"\nEnter {trans_type} amount: $")
        if not user_input.isdigit(): # When user enters letters
            continue
        return float(user_input)

# Check if user had enough funds
def withdraw_validattion(prev_balance) -> "float":
    '''
    user_amount -> input amount from user
    prev_amount -> current user balance
    return -> new current amount
    '''
    while True:
        user_amount = validate_user_input_amount("withdraw")
        print(user_amount, prev_balance)
        if user_amount > prev_balance:
            print(f"You  withdraw amount is greater than the current balance...\nTry a different amount!")
            continue
        return (user_amount, prev_balance - user_amount) # withdraw_amount

# Extra functions for user operations
# -----------------------------------------------------------------
def view_historical_trans():
    return
def category_assignment():
    return
def date_time_tracking():
    return
def user_describe_trans():
    return
def modefy_past_trans():
    return

# Checkbook file will start to run here
# -----------------------------------------------------------------
if __name__ == "__main__":
    print("\n~~~ Welcome to your terminal checkbook! ~~~\n")

    while True:

        # Make initial check of user input
        user_input = user_interface()

        # csv file to be user for user balance
        balance_file_name = "bonus_user_balance_file.csv"

        ## Conduct user operations
        if user_input == 1:
            curr_balance = view_curr_balance(balance_file_name)
            print(f"Current user balance: ${curr_balance}")

            # chek for continuation of interface
            responce = continue_transaction_propt()
            if responce:
                continue
            else:
                user_exit()
                break
                
        elif user_input == 2:
            # Get withdraw amount from user and current balance from file
            prev_balance = view_curr_balance(balance_file_name)
            user_amount, withdraw_amount = withdraw_validattion(prev_balance)

            new_balance = user_deposit_withdraw(balance_file_name, withdraw_amount)
            print(f"${float(user_amount)} has been withdrawn from ${prev_balance}")
            
            # Retreiving new balance
            new_curr_balance = view_curr_balance(balance_file_name)
            print(f"New acount balance: {new_curr_balance}")

            # chek for continuation of interface
            responce = continue_transaction_propt()
            if responce:
                continue
            else:
                user_exit()
                break

        elif user_input == 3:
            # Get deposit amount from user and current balance from file
            user_input = validate_user_input_amount("deposit")
            prev_balance = view_curr_balance(balance_file_name)

            # Adding user input to existing balance
            deposit_amount = float(user_input) + prev_balance
            new_balance = user_deposit_withdraw(balance_file_name, deposit_amount)
            print(f"${float(user_input)} has been added to ${prev_balance}")
            
            # Retreiving new balance
            new_curr_balance = view_curr_balance(balance_file_name)
            print(f"New acount balance: {new_curr_balance}")

            # chek for continuation of interface
            responce = continue_transaction_propt()
            if responce:
                continue
            else:
                user_exit()
                break

        elif user_input == 4:
            user_exit()
            break
        

        