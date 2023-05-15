import program_functions as pf
from datetime import datetime as dt

# Checkbook file will start to run here
# -----------------------------------------------------------------
if __name__ == "__main__":
    print("\n~~~ Welcome to your terminal checkbook! ~~~\n")

    while True:

        # Make initial check of user input
        user_input = pf.user_interface()

        # csv file to be user for user balance
        balance_file_name = "bonus_user_balance_file.csv"

        ## Conduct user operations
        if user_input == 1:
            transaction_type_toAdd = "View"
            primary_key, curr_balance, trans_type,transaction_date = pf.view_curr_balance(balance_file_name)

            print(f"Current user balance: ${curr_balance}")
            print(f"Transaction made on {dt.date(transaction_date)} at {dt.time(transaction_date)}")

            # Becuase viewing balance is another transaction, I add it to the balnce sheet
            pf.user_deposit_withdraw(balance_file_name, curr_balance, primary_key, transaction_type_toAdd)

            # chek for continuation of interface
            responce = pf.continue_transaction_propt()
            if responce:
                print("Would you like to explore more options? (yes or no)")
                continue
            else:
                pf.user_exit()
                break
                
        elif user_input == 2:
            transaction_type_toAdd = "Withdraw"

            # Get withdraw amount from user and current balance from file
            primary_key, prev_balance, trans_type,transaction_date = pf.view_curr_balance(balance_file_name)
            user_amount, withdraw_amount =pf.withdraw_validattion(prev_balance)

            # Adding user input to existing balance
            pf.user_deposit_withdraw(balance_file_name, withdraw_amount, primary_key, transaction_type_toAdd)
            print(f"\n${float(user_amount)} has been withdrawn from ${prev_balance}")
            
            # Retreiving new balance
            primary_key, new_curr_balance, trans_type, transaction_date = pf.view_curr_balance(balance_file_name)
            print(f"New acount balance: ${new_curr_balance}")
            print(f"Transaction make on {dt.date(transaction_date)} at {dt.time(transaction_date)}")

            # chek for continuation of interface
            responce = pf.continue_transaction_propt()
            if responce:
                continue
            else:
                pf.user_exit()
                break

        elif user_input == 3:
            transaction_type_toAdd = "Deposit"

            # Get deposit amount from user and current balance from file
            user_input = pf.validate_user_input_amount("deposit")
            primary_key, prev_balance, trans_type, transaction_date = pf.view_curr_balance(balance_file_name)

            # Adding user input to existing balance
            deposit_amount = user_input + prev_balance
            pf.user_deposit_withdraw(balance_file_name, deposit_amount, primary_key, transaction_type_toAdd)
            print(f"\n${float(user_input)} has been added to ${prev_balance}")
            
            # Retreiving new balance
            primary_key, new_curr_balance, trans_type, transaction_date = pf.view_curr_balance(balance_file_name)
            print(f"New acount balance: ${new_curr_balance}")
            print(f"Transaction make on {dt.date(transaction_date)} at {dt.time(transaction_date)}")

            # chek for continuation of interface
            responce = pf.continue_transaction_propt()
            if responce:
                continue
            else:
                pf.user_exit()
                break

        elif user_input == 4:
            pf.user_exit()
            break
        

        