from abc import ABCMeta, abstractmethod

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
    def create_account(self):
        pass
    def authenticate_user(self):
        pass
    def withdraw_sum(self):
        pass
    def deposit_sum(self):
        pass
    def display_balance(self):
        pass
    