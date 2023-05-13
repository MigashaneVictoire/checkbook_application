print("~~~ Welcome to your terminal checkbook! ~~~\n")
# get input from user
def get_user_input():
    return input("What would you like to do?\n")

def main_menu():
    print(f"1) view current balance \n2)record a debit (withdraw) \n3) record a credit (deposit) \n4) exit\n")

def invalid_input_propt():
    print("Please enter a valid input! \n\nEnter a number between 1 and 4\n")

if __name__ == "__main__":
    while True:
        main_menu()
        user_input = get_user_input()

        if user_input > 4:
            print(f"Invalid choice: {user_input}")
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        else:
            print("Thank you for visiting, have a great day!")
            break

        