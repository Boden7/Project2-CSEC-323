# @authors Brenden Shelton
# Date: 11/3/24
import unittest
from checkingAccount import CheckingAccount

class TestCheckingAccount(unittest.TestCase):
    
    def setUp(self):
        # Set up a CheckingAccount instance for each test
        print("\nSetting up accounts for testing...")
        self.account = CheckingAccount(100.0)  # Initial balance of 100.0
        self.other_account = CheckingAccount(50.0)  # Another account for transfer tests

    def test_initialization(self):
        # Test account initialization with initial balance:
        print("Testing account initialization...")
        self.assertEqual(self.account.getBalance(), 100.0)
    
    def test_deposit(self):
        # Test depositing funds into the account:
        print("Testing deposit function...")
        self.account.deposit(50.0)
        self.assertEqual(self.account.getBalance(), 150.0)
    
    def test_withdraw_within_balance(self):
        # Test withdrawing an amount within the balance: 
        print("Testing withdrawal within balance...")
        success = self.account.withdraw(30.0)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 70.0)
    
    def test_withdraw_exceeding_balance(self):
        # Test withdrawing an amount that exceeds the balance: 
        print("Testing withdrawal exceeding balance...")
        with self.assertRaises(AssertionError):
            self.account.withdraw(150)
        self.assertEqual(self.account.getBalance(), 100.0)  # Balance should remain unchanged
    
    def test_transfer(self):
        # Test transferring funds to another account: 
        print("Testing transfer between accounts...")
        success = self.account.transfer(20.0, self.other_account)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 80.0)
        self.assertEqual(self.other_account.getBalance(), 70.0)

    def test_calculate_interest(self):
        # Test interest calculation and application to balance: 
        print("Testing interest calculation...")
        self.account.calcInterest()
        expected_balance = 100.0 * (1 + 0.015)  # 1.5% interest applied
        self.assertAlmostEqual(self.account.getBalance(), expected_balance, places=2)
    
    def test_transaction_listing(self):
        # Test printing the transaction list: 
        print("Testing transaction listing...")
        self.account.deposit(50.0)
        self.account.withdraw(20.0)
        transactions = self.account.printTransactionList()
        self.assertNotEqual(transactions, "There are no valid transactions to display.")
    
    def test_write_transaction(self):
        # Test writing a transaction to the file with encryption: 
        print("Testing transaction write with encryption...")
        transaction = "test transaction"  # Dummy transaction
        self.account._writeTransaction(transaction)
        # Ensure no errors during the write process
    
    def test_read_transaction(self):
        # Test reading and decrypting transactions from file: 
        print("Testing transaction read with decryption...")
        self.account._readTransactions()
        # Ensure no errors during the read process

if __name__ == "__main__":
    unittest.main()
