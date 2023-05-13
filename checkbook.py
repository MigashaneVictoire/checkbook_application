import os
from curses.ascii import isdigit

# Functions to animate user interface
# -----------------------------------------------------------------
# get input from user
def get_user_input():
    return input("What would you like to do?\n")

# Print four options for the user
def main_menu():
    print(f"\n1) view current balance \n2)record a debit (withdraw) \n3) record a credit (deposit) \n4) exit\n")

# Propt the user to chose between the opetion
def invalid_input_propt():
    print("Please enter a valid input! \n-->Enter a number between 1 and 4\n")

# Functions to retreive data from checkbook
# -----------------------------------------------------------------
def check_file_exists(balance_file_name) -> "string":
    '''
    Will create file if file don't exist
    '''
    if os.path.exists(balance_file_name):
        with open(balance_file_name, "r") as balance_file:
            balance_file_lines = balance_file.readlines()
            return balance_file_lines
    else:
        # creating a new file
        print(f"File {balance_file_name} not found... \nCreating file...")
        with open(balance_file_name, "w") as balance_file:
            balance_file.write("0")
            print(f"File {balance_file_name} has been created!")

def view_curr_balance():
    return

def user_withdraw():
    return

def user_deposit():
    return
def user_exit():
    return

# Checkbook file will start here
# -----------------------------------------------------------------
if __name__ == "__main__":

    print("\n~~~ Welcome to your terminal checkbook! ~~~\n")

    # make initial check of user input
    while True:
        main_menu()
        user_input = get_user_input()
        if not user_input.isdigit(): # when user enters letters
            continue
        else:
            if int(user_input) > 4:
                invalid_input_propt() # # user input not in range 4
                continue
            user_input = int(user_input)
            break

    balance_file_name = "user_balance_file.txt"
    if user_input == 1:
        balance = check_file_exists(balance_file_name)
        print(balance)

        # check current balance and report to user
        # if len(balance) == 0:
        #     print("Your current balance is $0.00")
        # else:
        #     print(balance)
            
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    else:
        print("Thank you for visiting, have a great day!")
        

        