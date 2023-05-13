import os
import csv
from curses.ascii import isdigit

# Functions to animate user interface
# -----------------------------------------------------------------
# Get input from user
def get_user_input():
    return input("What would you like to do?\n")

# Print four options for the user
def main_menu():
    print(f"\n1) view current balance \n2)record a debit (withdraw) \n3) record a credit (deposit) \n4) exit\n")

# Propt the user to chose between the opetion
def invalid_input_propt():
    print("Please enter a valid input! \n-->Enter a number between 1 and 4\n")

# Exit program
def user_exit():
    return

# Functions to retreive data from checkbook
# -----------------------------------------------------------------
# Check existance of file
def check_file_exists(balance_file_name) -> str:
    '''
    balance_file_name -> string representing the csv file to be found
    --> Will create file if file don't exist
    '''
    if os.path.exists(balance_file_name):
        # Open the existing file and retreive the balance
        with open(balance_file_name, "r") as balance_file:
            balance_file_lines = balance_file.readlines()
            return balance_file_lines
    else:
        # Creating a new file with a cell holding 0
        print(f"File {balance_file_name} not found... \nCreating file...")
        balance_file = csv.writer(open(balance_file_name, "w"), dialect='excel')
        balance_file.writerow([0])
        return f"File {balance_file_name} has been created!"

# Show current balance
def view_curr_balance(balance_file_name) -> str:
    '''
    balance_file_name -> string representing the csv file to be found
    balance -> iniciate balance file
    curr_balance -> balance is returned as integer after replacing \\n
    '''
    balance = check_file_exists(balance_file_name) # Retreive file

    # Check current balance and report to user
    if len(balance) == 1:
        print("Your current balance is $0.00")
    else:
        curr_balance = float(balance[-1].replace('\n', ""))
        return curr_balance 

# Substract funds from balance
def user_withdraw(balance_file_name, withdraw_amount) -> "str, float":
    '''
    balance_file_name -> string representing the csv file to be found
    deposit_amount -> orinal cheeckbook balance - user input amount
    balance_file -> iniciate append sequence in the csv file
    '''
    balance_file = csv.writer(open(balance_file_name, 'a'), dialect='excel')
    balance_file.writerow([withdraw_amount])

# Add funds to balance
def user_deposit(balance_file_name, deposit_amount) -> 'str, float':
    '''
    balance_file_name -> string representing the csv file to be found
    deposit_amount -> user input amount + orinal cheeckbook balance
    balance_file -> iniciate append sequence in the csv file
    '''
    balance_file = csv.writer(open(balance_file_name, 'a'), dialect='excel')
    balance_file.writerow([deposit_amount])


# Checkbook file will start here
# -----------------------------------------------------------------
if __name__ == "__main__":

    print("\n~~~ Welcome to your terminal checkbook! ~~~\n")

    # Make initial check of user input
    while True:
        main_menu()
        user_input = get_user_input()
        if not user_input.isdigit(): # When user enters letters
            continue
        else:
            if int(user_input) > 4:
                invalid_input_propt() # # User input not in range 4
                continue
            user_input = int(user_input)
            break

    # csv file to be user for user balance
    balance_file_name = "user_balance_file.csv"

    ## Conduct user operations
    if user_input == 1:
        curr_balance = view_curr_balance(balance_file_name)
        print(curr_balance)
            
    elif user_input == 2:
        # Get deposit amount from user and current balance from file
        user_input = input("\nEnter deposit amount: ")
        prev_balance = view_curr_balance(balance_file_name)

        # Adding user input to existing balance
        withdraw_amount = prev_balance - float(user_input)
        new_balance = user_deposit(balance_file_name, withdraw_amount)
        print(f"${float(user_input)} has been withdrawn from {prev_balance}")
        
        # Retreiving new balance
        new_curr_balance = view_curr_balance(balance_file_name)
        print(f"New acount balance: {new_curr_balance}")

    elif user_input == 3:
        # Get deposit amount from user and current balance from file
        user_input = input("\nEnter deposit amount: ")
        prev_balance = view_curr_balance(balance_file_name)

        # Adding user input to existing balance
        deposit_amount = float(user_input) + prev_balance
        new_balance = user_deposit(balance_file_name, deposit_amount)
        print(f"${float(user_input)} has been added to {prev_balance}")
        
        # Retreiving new balance
        new_curr_balance = view_curr_balance(balance_file_name)
        print(f"New acount balance: {new_curr_balance}")
    else:
        print("Thank you for visiting, have a great day!")
        

        