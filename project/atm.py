class BankAccount:

    def __init__(self, name, pin, balance):
        self.account_holder_name = name       # Public
        self.__pin = pin                     # Private
        self.__balance = balance             # Private
        self.__attempts = 0
        self.__blocked = False

    # Verify PIN
    def verify_pin(self, pin):
        if self.__blocked:
            raise Exception("Account is blocked due to 3 incorrect PIN attempts.")

        if pin == self.__pin:
            self.__attempts = 0
            return True
        else:
            self.__attempts += 1
            remaining = 3 - self.__attempts

            if self.__attempts >= 3:
                self.__blocked = True
                raise Exception("3 incorrect attempts. Account is blocked.")

            print("Incorrect PIN.")
            print("Attempts remaining:", remaining)
            return False

    # Check balance
    def check_balance(self, pin):
        if self.verify_pin(pin):
            return self.__balance

    # Deposit money
    def deposit(self, amount, pin):
        if self.verify_pin(pin):
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than 0.")

            self.__balance += amount
            print("Amount deposited successfully.")
            print("Current balance:", self.__balance)

    # Withdraw money
    def withdraw(self, amount, pin):
        if self.verify_pin(pin):
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than 0.")

            if amount > self.__balance:
                raise ValueError("Insufficient balance.")

            self.__balance -= amount
            print("Amount withdrawn successfully.")
            print("Current balance:", self.__balance)

    # Change PIN
    def change_pin(self, old_pin, new_pin):

        if self.verify_pin(old_pin):

            if len(str(new_pin)) != 4:
                raise ValueError("New PIN must contain exactly 4 digits.")

            self.__pin = new_pin
            print("PIN changed successfully.")


# Creating account
account = BankAccount("Harsha", 1234, 5000)


# Menu-driven ATM
while True:

    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")
    print("==============================")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            pin = int(input("Enter PIN: "))
            balance = account.check_balance(pin)

            if balance is not None:
                print("Current Balance:", balance)

        elif choice == 2:

            pin = int(input("Enter PIN: "))
            amount = float(input("Enter deposit amount: "))

            account.deposit(amount, pin)

        elif choice == 3:

            pin = int(input("Enter PIN: "))
            amount = float(input("Enter withdrawal amount: "))

            account.withdraw(amount, pin)

        elif choice == 4:

            old_pin = int(input("Enter old PIN: "))
            new_pin = int(input("Enter new 4-digit PIN: "))

            account.change_pin(old_pin, new_pin)

        elif choice == 5:

            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please select 1-5.")

    except ValueError as e:
        print("Invalid input:", e)

    except Exception as e:
        print("Error:", e)