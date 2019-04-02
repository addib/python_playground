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
    def _init_(self):
        self.savings_accounts = {}

    def create_account(self, name, initial_deposit):
        self.account_number = randint(1000000000, 9999999999)
        self.savings_accounts[self.account_number] = [name, initial_deposit]

    def authenticate_user(self, name, account_number):
        if account_number in self.savings_accounts.keys():
            if self.savings_accounts[self.account_number][0] == name:
                print("Authentication successful")
                self.account_number = account_number
                return True
            else:
                print("Name does not match")
                return False
        else:
            print("Account number not valid")
            return False

    def withdraw_sum(self, withdrawl_sum):
        if withdrawl_sum > self.savings_accounts[self.account_number][1]:
            print("Insufficient balance")
        else:
            self.savings_accounts[self.account_number][1] -= withdrawl_sum
            print("Withdrawl successful. Available balance: ", end = " ")
            self.display_balance()
    
    def deposit_sum(self, deposited_sum):
        self.savings_accounts[self.account_number][1] += deposited_sum
        print("Deposit successful. Available balance: ", end = " ")
        self.display_balance()

    def display_balance(self):
        print("Available balance: ", self.savings_accounts[self.account_number][1])

SavingsAccount = SavingsAccount()