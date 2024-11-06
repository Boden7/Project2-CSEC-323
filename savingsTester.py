import unittest
from savingsAccount import SavingsAccount
from transaction import Transaction
from unittest.mock import patch, MagicMock

class TestSavingsAccount(unittest.TestCase):

    # Test the creation of a SavingsAccount with an initial balance
    def test_initialization(self):
        # Test default initialization with zero balance
        account = SavingsAccount()
        self.assertEqual(account.getBalance(), 0.0)
        self.assertEqual(account.getOverdrawnCount(), 0)

        # Test initialization with a specific balance
        account2 = SavingsAccount(500.0)
        self.assertEqual(account2.getBalance(), 500.0)

    # Test deposit method (positive amount)
    def test_deposit(self):
        account = SavingsAccount(100.0)
        
        # Deposit a valid positive amount
        success = account.deposit(50.0)
        self.assertTrue(success)
        self.assertEqual(account.getBalance(), 150.0)

    # Test deposit method (negative amount, should raise an assertion error)
    def test_deposit_invalid(self):
        account = SavingsAccount(100.0)
        with self.assertRaises(AssertionError):
            account.deposit(-50.0)

    # Test withdraw method (valid withdrawal)
    def test_withdraw(self):
        account = SavingsAccount(1000.0)
        
        # Withdraw a valid amount
        success = account.withdraw(200.0)
        self.assertTrue(success)
        self.assertEqual(account.getBalance(), 800.0)

    # Test withdraw method (insufficient balance, should apply overdraft fee)
    def test_withdraw_overdraft(self):
        account = SavingsAccount(50.0)
        
        # Withdraw an amount greater than balance
        success = account.withdraw(100.0)
        self.assertTrue(success)
        self.assertEqual(account.getBalance(), 50.0 - account.getOverdraft())
        
        # Ensure the overdraft count is incremented
        self.assertEqual(account.getOverdrawnCount(), 1)

    # Test withdraw method (too many overdrafts, should deny withdrawal)
    def test_withdraw_too_many_overdrafts(self):
        account = SavingsAccount(50.0)
        account._setOverdrawnCount(3)  # Simulate too many overdrafts

        with self.assertRaises(AssertionError):
            account.withdraw(100.0)

    # Test transfer between accounts
    def test_transfer(self):
        account1 = SavingsAccount(1000.0)
        account2 = SavingsAccount(500.0)

        success = account1.transfer(200.0, account2)
        self.assertTrue(success)
        self.assertEqual(account1.getBalance(), 800.0)
        self.assertEqual(account2.getBalance(), 700.0)

    # Test interest calculation and deposit into the account
    def test_calc_interest(self):
        account = SavingsAccount(1000.0)
        
        # Assume the interest rate for savings accounts is 0.02 (2%)
        account.calcInterest()
        self.assertEqual(account.getBalance(), 1000.0 * 1.02)  # Balance should have increased by 2%

    # Test getting the overdraft fee
    def test_get_overdraft(self):
        account = SavingsAccount(100.0)
        account._setOverdrawnCount(1)
        
        overdraft_fee = account.getOverdraft()
        self.assertEqual(overdraft_fee, 30.00)  # Based on the `_overdraftFee` list

    # Test printing the transaction list
    def test_print_transaction_list(self):
        account = SavingsAccount(500.0)
        account.deposit(100.0)
        
        with patch('builtins.print') as mocked_print:
            account.printTransactionList()
            mocked_print.assert_called()  # Check that print was called for transactions

    # Test write and read transactions (mocking file operations)
    @patch('builtins.open', new_callable=MagicMock)
    def test_write_transactions(self, mock_file):
        account = SavingsAccount(500.0)
        transaction = Transaction("deposit", 100.0)
        account._writeTransaction(transaction)
        
        # Ensure the file was written to
        mock_file.assert_called_with("savings.txt", "wb")

    @patch('builtins.open', new_callable=MagicMock)
    def test_read_transactions(self, mock_file):
        account = SavingsAccount(500.0)
        
        # Simulate a file read
        mock_file.return_value.__enter__.return_value.readline.return_value = b'100'
        account.readTransactions()

        mock_file.assert_called_with("savings.txt", "rb")

    # Test transaction logging with a mock transaction
    def test_transaction_logging(self):
        account = SavingsAccount(1000.0)
        account.deposit(200.0)
        
        transaction_list = account._accountTransactions
        self.assertEqual(len(transaction_list), 1)
        self.assertEqual(transaction_list[0].getType(), "deposit")
        self.assertEqual(transaction_list[0].getAmount(), 200.0)

    # Test the representation method (__repr__)
    def test_repr(self):
        account = SavingsAccount(500.0)
        account.deposit(100.0)
        
        repr_output = repr(account)
        self.assertIn("Account Number:", repr_output)
        self.assertIn("Balance: 600.00", repr_output)
        self.assertIn("Account Type: 'savings'", repr_output)

if __name__ == '__main__':
    unittest.main()
