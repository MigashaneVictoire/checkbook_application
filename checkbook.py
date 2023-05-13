import os
from curses.ascii import isdigit

# Functions to animate user interface
# -----------------------------------------------------------------
# get input from user
def get_user_input():
    return input("What would you like to do?\n")

def main_menu():
    print(f"\n1) view current balance \n2)record a debit (withdraw) \n3) record a credit (deposit) \n4) exit\n")

def invalid_input_propt():
    print("Please enter a valid input! \n-->Enter a number between 1 and 4\n")

# Functions to retreive data from checkbook
# -----------------------------------------------------------------
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

    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    else:
        print("Thank you for visiting, have a great day!")
        

        