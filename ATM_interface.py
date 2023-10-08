# Import the tabulate module for formatting data into tables and the sys module for system-specific functions.
from tabulate import tabulate
import sys

# Define a class named "ATM" to represent the ATM functionality.
class ATM:
    # Initialize the ATM with an initial balance, current balance, and an empty transaction history.
    def __init__(self):
        self.initial_balance = 100000
        self.balance = self.initial_balance
        self.transaction_history = []

    # Define a method for depositing money into the ATM.
    def deposit(self, amount):
        # Increase the balance by the deposited amount.
        self.balance += amount
        # Create a transaction detail message for the deposit and append it to the transaction history.
        transaction_detail = f'Deposited ${amount}'
        self.transaction_history.append(transaction_detail)
        # Return a message confirming the deposit and showing the new balance.
        return f'Deposited ${amount}. New balance: ${self.balance}'

    # Define a method for withdrawing money from the ATM.
    def withdraw(self, amount):
        # Check if the requested withdrawal amount is less than or equal to the available balance.
        if amount <= self.balance:
            # Reduce the balance by the withdrawn amount.
            self.balance -= amount
            # Create a transaction detail message for the withdrawal and append it to the transaction history.
            self.transaction_history.append(f'Withdrawn ${amount}')
            # Return a message confirming the withdrawal and showing the new balance.
            return f'Withdrawn ${amount}. New balance: ${self.balance}'
        else:
            # Return an "Insufficient funds" message if the withdrawal amount exceeds the available balance.
            return 'Insufficient funds'


    # Define a method for transferring money from the ATM to another recipient.
    def transfer(self, amount, recipient, transfer_type):
        # Check if the requested transfer amount is less than or equal to the available balance.
        if amount <= self.balance:
            # Reduce the balance by the transferred amount based on the transfer type.
            self.balance -= amount
            # Create a transaction detail message for the transfer based on the transfer type.
            if transfer_type == 1:
                transaction_detail = f'Transferred ${amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            elif transfer_type == 2:
                transaction_detail = f'Transferred ${amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            elif transfer_type == 3:
                transaction_detail = f'Transferred ${amount} to {recipient}'
                # Append the transaction detail to the transaction history.
                self.transaction_history.append(transaction_detail)
            # Return a message confirming the transfer and showing the new balance.
            return f'Transferred ${amount} to {recipient}. New balance: ${self.balance}'
        else:
            # Return an "Insufficient funds" message if the transfer amount exceeds the available balance.
            return 'Insufficient funds'

    # Define a method to get the current balance.
    def get_balance(self):
        # Return a message displaying the current balance.
        return f'Current balance: ${self.balance}'

    # Define a method to get the transaction history.
    def get_transaction_history(self):
        # Return the list of transaction history.
        return self.transaction_history
    

    # Function to display ATM logo
def display_logo():
    # Define the ASCII art for the "Welcome" logo
    welcome_logo = """

 ▄ .▄▄▄▄· ▄▄▄·▄▄▄·▄· ▄▌     ▄▄·     ·▄▄▄▄ ▪  ▐ ▄ ▄▄ •     ▄▄ 
██▪▐▐█ ▀█▐█ ▄▐█ ▄▐█▪██▌    ▐█ ▌▪    ██▪ ████•█▌▐▐█ ▀ ▪    ██▌
██▀▐▄█▀▀█ ██▀·██▀▐█▌▐█▪    ██ ▄▄▄█▀▄▐█· ▐█▐█▐█▐▐▄█ ▀█▄    ▐█·
██▌▐▐█ ▪▐▐█▪·▐█▪·•▐█▀·.    ▐███▐█▌.▐██. ██▐███▐█▐█▄▪▐█    .▀ 
▀▀▀ ·▀  ▀.▀  .▀    ▀ •     ·▀▀▀ ▀█▄▀▀▀▀▀▀•▀▀▀▀ █·▀▀▀▀      ▀ 


 █     █▓█████ ██▓    ▄████▄  ▒█████  ███▄ ▄███▓█████     ▐██▌    
▓█░ █ ░█▓█   ▀▓██▒   ▒██▀ ▀█ ▒██▒  ██▓██▒▀█▀ ██▓█   ▀     ▐██▌    
▒█░ █ ░█▒███  ▒██░   ▒▓█    ▄▒██░  ██▓██    ▓██▒███       ▐██▌    
░█░ █ ░█▒▓█  ▄▒██░   ▒▓▓▄ ▄██▒██   ██▒██    ▒██▒▓█  ▄     ▓██▒    
░░██▒██▓░▒████░██████▒ ▓███▀ ░ ████▓▒▒██▒   ░██░▒████▒    ▒▄▄     
░ ▓░▒ ▒ ░░ ▒░ ░ ▒░▓  ░ ░▒ ▒  ░ ▒░▒░▒░░ ▒░   ░  ░░ ▒░ ░    ░▀▀▒    
  ▒ ░ ░  ░ ░  ░ ░ ▒  ░ ░  ▒    ░ ▒ ▒░░  ░      ░░ ░  ░    ░  ░    
  ░   ░    ░    ░ ░  ░       ░ ░ ░ ▒ ░      ░     ░          ░    
    ░      ░  ░   ░  ░ ░         ░ ░        ░     ░  ░    ░       
                     ░                                            
                                                                                                                

    """

    # Display the logo in the console
    print(welcome_logo)


# Define a function named "atm_interface" to handle the ATM user interface.
def atm_interface():

    # Create an instance of the ATM class.
    atm = ATM()

    # Call the "display_logo" function to display the ATM logo.
    display_logo()  # Display the ATM logo
    # Print a welcome message.
    print("Welcome to the ATM Interface")

    # Prompt the user to enter a User ID and PIN.
    user_id = input("Enter User ID: ")
    pin = input("Enter PIN: ")

    # Check if the entered User ID and PIN are valid.
    if user_id == "123456" and pin == "654321":
        print("Login successful!\n")

        while True:
            # Display the available ATM operations to the user.
            print("ATM Operations:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Quit")

            # Prompt the user to enter their choice.
            choice = input("Enter your choice (1/2/3/4/5/6): ")

            if choice == "1":
                # Prompt the user to enter the deposit amount and pass_code.
                amount = float(input("Enter the deposit amount: $"))
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                # Call the "deposit" method and display the result.
                result = atm.deposit(amount)
                print(f"{result}\npass_code: {pass_code_display}")
            elif choice == "2":
                # Prompt the user to enter the withdrawal amount and pass_code.
                amount = float(input("Enter the withdrawal amount: $"))
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                # Call the "withdraw" method and display the result.
                result = atm.withdraw(amount)
                print(f"{result}\npass_code: {pass_code_display}")
            elif choice == "3":
                # Display options for different transfer types.
                print("Choose Transfer Type:")
                print("1. Account Transfer")
                print("2. Phone Transfer")
                print("3. Card Transfer")
                # Prompt the user to select a transfer type.
                transfer_type = int(input("Enter your choice (1/2/3): "))

                # Prompt the user to enter the transfer amount and recipient's name.
                amount = float(input("Enter the transfer amount: $"))
                recipient = input("Enter the recipient's name: ")

                transfer_details = f"Recipient: {recipient}"

                if transfer_type == 1:
                    # Prompt the user to enter recipient's account number, IFSC code, and pass_code.
                    account_no = input("Enter recipient's account number: ")
                    ifsc_code = input("Enter recipient's account IFSC code: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    # Update transfer_details and call the "transfer" method.
                    transfer_details = f"Recipient: {recipient}\nAccount: {account_no}\nIFSC: {ifsc_code}\nPasscode: {pass_code_display}"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                elif transfer_type == 2:
                    # Prompt the user to enter recipient's phone number, UPI ID, and pass_code.
                    phone_number = input("Enter recipient's phone number: ")
                    upi_id = input("Enter UPI ID: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    # Update transfer_details and call the "transfer" method.
                    transfer_details = f"Recipient: {recipient}\nPhone: {phone_number}\nUPI: {upi_id}\nPasscode: {pass_code_display}"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                elif transfer_type == 3:
                    # Prompt the user to enter recipient's card number and pass_code.
                    card_number = input("Enter recipient's card number: ")
                    pass_code = input("Enter 4 or 6 digit pass_code: ")
                    pass_code_display = '*' * len(pass_code)
                    # Update transfer_details and call the "transfer" method.
                    transfer_details = f"Recipient: {recipient}\nCard: {card_number}\nPasscode: {pass_code_display}"
                    result = atm.transfer(amount, transfer_details, transfer_type)
                else:
                    # Return an error message for an invalid transfer type.
                    result = "Invalid transfer type selection."
                    transfer_details = "N/A"
                # Print the result of the transfer.
                print(result)
            elif choice == "4":
                # Call the "get_balance" method and display the balance along with pass_code masking.
                balance = atm.get_balance()
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)
                print(f"{balance}\npass_code: {pass_code_display}\nAvailable Balance: ${atm.balance:.2f}")
            # Check if the user's choice is "5" (Transaction History).
            elif choice == "5":
                # Prompt the user to enter a 4 or 6 digit pass_code.
                pass_code = input("Enter 4 or 6 digit pass_code: ")
                pass_code_display = '*' * len(pass_code)

                # Set the pass_code attribute of the ATM instance to the entered pass_code.
                atm.pass_code = pass_code
            
                # Get the transaction history from the ATM.
                history = atm.get_transaction_history()
                
                # Check if there are transactions in the history.
                if len(history) > 0:
                    # Initialize an empty list to store the transaction table.
                    table = []
                    # Initialize the available_balance with the initial_balance of the ATM.
                    available_balance = atm.initial_balance
                    # Loop through each transaction in the history.
                    for i, transaction in enumerate(history, start=1):
                        # Split the transaction string by the dollar sign and take the last part
                        transaction_parts = transaction.split('$')
                        if len(transaction_parts) > 1:
                            # Extract the transaction amount from the split transaction string.
                            transaction_amount = float(transaction_parts[-1].split()[0])
                            
                            # Update available_balance based on the type of transaction.
                            if "Deposited" in transaction:
                                available_balance += transaction_amount
                            elif "Withdrawn" in transaction or "Transferred" in transaction:
                                available_balance -= transaction_amount
                        
                        # Create a row for the table with the transaction number, details, and available balance.
                        table.append([i, transaction, f"${available_balance:.2f}"])
                    # Display the transaction history table using tabulate.
                    print(tabulate(table, headers=["#", "Transaction", "Available Balance"], tablefmt="grid"))
                else:
                    # If the transaction history is empty, print a message.
                    print("Transaction history is empty.")

            # Check if the user's choice is "6" (Quit).
            elif choice == "6":
                # Print a thank you message and break out of the loop to exit the program.
                print("Thank you for using ATM. Goodbye!")
                break
            # Check if the user's choice is not a valid option.
            else:
                print("Invalid choice. Please enter a valid option.")

        # Check if the user wants to continue using the ATM
        continue_choice = input("Do you want to perform another transaction? (yes/no): ")
        # Check if the user's response is not "yes" (i.e., they want to quit).
        if continue_choice.lower() != "yes":
            # Print a thank you message and exit the program.
            print("Thank you for using ATM. Goodbye!")
    # Check if the provided User ID and PIN are invalid.
    else:
        print("Invalid User ID or PIN. Exiting...")
        sys.exit() 

# Check if the script is being run as the main program.
if __name__ == "__main__":
    # Call the "atm_interface" function to start the ATM application.
    atm_interface()
