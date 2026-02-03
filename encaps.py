#you are given a bank account class, the account balance must not be accessed directly, only deposit() and withdraw() operations are allowed, Task: Implement data hiding so that balance cannot be modified directly, use pytest
import pytest
class BankAccount:
    def __init__(self):
        self.__balance = 0 
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance
def test_bank_account():
    account = BankAccount()
    assert account.get_balance()==0
    account.deposit(100)
    assert account.get_balance()==100
    account.withdraw(50)
    assert account.get_balance()==50
    account.withdraw(100)  
    assert account.get_balance()==50

    

if __name__=="__main__":
    pytest.main()