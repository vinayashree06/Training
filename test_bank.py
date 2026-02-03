import unittest

class Bank:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amt):
        self.balance += amt
        return self.balance

class TestBank(unittest.TestCase):
    def test_deposit(self):
        bank = Bank()
        result = bank.deposit(1000)
        self.assertEqual(result, 1000)

    @unittest.skip("demonstrating skipping")
    def test_future(self):
        pass

if __name__ == "__main__":
    unittest.main()
