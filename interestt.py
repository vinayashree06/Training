from abc import ABC, abstractmethod
class Bank(ABC):
    def __init__(self, amount):
        self.amount = amount
    @abstractmethod
    def calculate_interest(self):
        pass
    def display(self):
        print("Principal Amount:", self.amount)
class SBI(Bank):
    def calculate_interest(self):
        interest = self.amount * 0.05
        print("SBI Interest:", interest)
class HDFC(Bank):
    def calculate_interest(self):
        interest = self.amount*0.07
        print("HDFC Interest:", interest)
class ICICI(Bank):
    def calculate_interest(self):
        interest = self.amount*0.065
        print("ICICI Interest:",interest)
amount = int(input("Enter deposit amount:"))
banks = [SBI(amount), HDFC(amount), ICICI(amount)]
for bank in banks:
    bank.display()
    bank.calculate_interest()
    print()
