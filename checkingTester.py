# @authors Brenden Shelton
# Date: 11/3/24
import unittest
from checkingAccount import CheckingAccount

# @authors Brenden Shelton
# Date: 11/3/24
import unittest
from checkingAccount import CheckingAccount

class TestCheckingAccount(unittest.TestCase):
    
    def setUp(self):
        """Set up a CheckingAccount instance before each test."""
        # Initialize a CheckingAccount with a starting balance of 100.0
        self.account = CheckingAccount(100.0)
        # Create another account for testing transfers
        self.other_account = CheckingAccount(50.0)

    def test_initialization(self):
        """Test account initialization with initial balance."""
        self.assertEqual(self.account.getBalance(), 100.0)
    
    def test_deposit(self):
        """Test depositing funds into the account."""
        self.account.deposit(50.0)
        self.assertEqual(self.account.getBalance(), 150.0)
    
    def test_withdraw_within_balance(self):
        """Test withdrawing an amount within the balance."""
        success = self.account.withdraw(30.0)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 70.0)
    
    def test_withdraw_exceeding_balance(self):
        """Test withdrawing an amount that exceeds the balance."""
        success = self.account.withdraw(150.0)  # Should fail
        self.assertFalse(success)
        self.assertEqual(self.account.getBalance(), 100.0)  # Balance should remain unchanged
    
    def test_transfer(self):
        """Test transferring funds to another account."""
        success = self.account.transfer(20.0, self.other_account)
        self.assertTrue(success)
        self.assertEqual(self.account.getBalance(), 80.0)
        self.assertEqual(self.other_account.getBalance(), 70.0)

if __name__ == '__main__':
    unittest.main()
