class ATM:
    def __init__(self, card_number, balance=0, pin=1234):
        self.card_number = card_number
        self.balance = balance
        self.pin = pin
        self.history = []

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def balance_inquiry(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: {amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew: {amount}")
            return True
        return False

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.history.append("PIN changed successfully")
            return True
        return False

    def transaction_history(self):
        return self.history if self.history else ["No transactions yet"]

# Sample interaction with the ATM class
def main():
    print("Welcome to the ATM machine!")
    card_number = input("Please enter your card number: ")
    atm = ATM(card_number, balance=1000)

    while True:
        print("\nSelect an option:")
        print("1. Account Balance Inquiry")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. PIN Change")
        print("5. Transaction History")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice in {1, 3, 4}:  # Options that require PIN entry
            entered_pin = int(input("Enter your PIN: "))
            if not atm.check_pin(entered_pin):
                print("Incorrect PIN!")
                continue  # Return to the main menu

        if choice == 1:
            print(f"Your account balance is: {atm.balance_inquiry()}")
                
        elif choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            if atm.deposit(amount):
                print(f"{amount} deposited successfully!")
            else:
                print("Invalid amount!")
                
        elif choice == 3:
            amount = float(input("Enter the amount to withdraw: "))
            if atm.withdraw(amount):
                print(f"{amount} withdrawn successfully!")
            else:
                print("Insufficient balance or invalid amount!")
                
        elif choice == 4:
            new_pin = int(input("Enter your new PIN: "))
            if atm.change_pin(entered_pin, new_pin):
                print("PIN changed successfully!")
            else:
                print("Error changing PIN!")
                
        elif choice == 5:
            print("Transaction History:")
            for transaction in atm.transaction_history():
                print(transaction)

        elif choice == 6:
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
