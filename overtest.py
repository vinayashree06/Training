#Method Overriding bank interest, A base class Bank defines a method, getInterestRate(),Different banks have different interest rates, Task: Override the getInterestRate() method in each subclass, use punittest, task:Override the method in child classes.
import unittest
class Bank:
    def getInterestRate(self):
        pass
class SBI(Bank):
    def getInterestRate(self):
        return 7.0
class ICICI(Bank):
    def getInterestRate(self):
        return 7.5
class TestBankInterestRate(unittest.TestCase):
    def test_sbi_interest_rate(self):
        sbi = SBI()
        self.assertEqual(sbi.getInterestRate(), 7.0)
    def test_icici_interest_rate(self):
        icici = ICICI()
        self.assertEqual(icici.getInterestRate(), 7.5)
if __name__=='__main__':
    unittest.main()