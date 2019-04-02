from abc import ABCMeta, abstractmethod
from random import randint

# abstract base class to enforce methods on the derived child class SavingsAccount
class Account(metaclass = ABCMeta):
    @abstractmethod
    def create_account():
        return 0
    @abstractmethod
    def authenticate_user():
        return 0
    @abstractmethod
    def withdraw_sum():
        return 0
    @abstractmethod
    def deposit_sum():
        return 0
    @abstractmethod
    def display_balance():
        return 0


class SavingsAccount:
    def __init__(self):
        self.savings_accounts = {}

    def create_account(self, name, initial_deposit):
        self.account_number = randint(1000000000, 9999999999)
        self.savings_accounts[self.account_number] = [name, initial_deposit]
        print("[INFO]: Account creation successful! Your account number is: ", self.account_number)

    def authenticate_user(self, name, account_number):
        if account_number in self.savings_accounts.keys():
            if self.savings_accounts[self.account_number][0] == name:
                print("[INFO]: Authentication successful!")
                self.account_number = account_number
                return True
            else:
                print("[ALERT]: Name does not match!")
                return False
        else:
            print("[ALERT]: Account number not valid!")
            return False

    def withdraw_sum(self, withdrawal_sum):
        if withdrawal_sum > self.savings_accounts[self.account_number][1]:
            print("[ALERT]: Insufficient balance!")
        else:
            self.savings_accounts[self.account_number][1] -= withdrawal_sum
            print("[INFO]: Withdrawal successful!", end = " ")
            self.display_balance()
    
    def deposit_sum(self, deposited_sum):
        self.savings_accounts[self.account_number][1] += deposited_sum
        print("[INFO]: Deposit successful!", end = " ")
        self.display_balance()

    def display_balance(self):
        print("Your available balance is Rs.", self.savings_accounts[self.account_number][1])

savingsAccount = SavingsAccount()

while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    user_choice = int(input())

    if user_choice is 1:
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savingsAccount.create_account(name, deposit)
    elif user_choice is 2:
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        account_number = int(input())
        authentication_status = savingsAccount.authenticate_user(name, account_number)
        if authentication_status is True:
            while True:
                print("Enter 1 to withdraw amount")
                print("Enter 2 to deposit amount")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous menu")
                user_choice = int(input())

                if user_choice is 1:
                    print("Enter the withdrawal amount: ")
                    withdrawal_amount = int(input())
                    savingsAccount.withdraw_sum(withdrawal_amount)
                elif user_choice is 2:
                    print("Enter the deposit amount: ")
                    deposit_amount = int(input())
                    savingsAccount.deposit_sum(deposit_amount)
                elif user_choice is 3:
                    savingsAccount.display_balance()
                elif user_choice is 4:
                    break
    elif user_choice is 3:
        exit()
