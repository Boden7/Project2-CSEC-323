# @authors Brenden Shelton
# Date: 11/3/24
import unittest
from checkingAccount import CheckingAccount

class CheckingAccountTester(unittest.TestCase):
    def setUp(self):
        # Resets the checking account number for each test
        CheckingAccount._nextAccountVal = 2000
        # Constructs an empty CheckingAccount object
        # Parameters: First name = "John", Last name = "Doe", Balance = 100.0,
        # Account Transactions = [], Overdrawn Count = 0, Account Number = 2000
        self.testObject = CheckingAccount("John", "Doe", 100.0)
        
        # Constructs a valid CheckingAccount object with no balance parameter
        # Parameters: First name = "John", Last name = "Doe", Balance = 0.0,
        # Account Transactions = [], Overdrawn Count = 0, Account Number = 2001        
        self.testObject2 = CheckingAccount("John", "Doe")        

    def test_ConstructorValid(self):
        # Ensures the CheckingAccount object was created successfully
        self.assertTrue(isinstance(self.testObject, CheckingAccount))

    def test_ConstructorInvalidFirstNameBlank(self):
        # Ensures an empty first name raises an assertion error
        self.assertRaises(AssertionError, CheckingAccount, "", "Doe", 100.0)

    def test_ConstructorInvalidLastNameSpecialChar(self):
        # Ensures a last name with special characters raises an assertion error        
        self.assertRaises(AssertionError, CheckingAccount, "John", "!@#$%", 100.0)        

    def test_ConstructorInvalidBalanceType(self):
        # Ensures a non-numeric balance raises an assertion error        
        self.assertRaises(AssertionError, CheckingAccount, "John", "Doe", "100.0")

    def test_getAccountNumber(self):
        # Checks that the account number starts from 2000
        accountNum = self.testObject.getAccountNumber()
        self.assertEqual(accountNum, 2000)

    def testDeposit(self):
        # Initializes balance to 0
        self.testObject._balance = 0.0
        # Adds 50 to the balance
        result = self.testObject.deposit(50.0)
        # Ensures deposit was successful
        self.assertEqual(result, True)
        # Ensures the balance is updated correctly
        self.assertEqual(self.testObject.getBalance(), 50.0)

    def testFailedDeposit(self):
        # Attempts to deposit a negative amount
        result = self.testObject.deposit(-50.0)
        # Ensures deposit was rejected
        self.assertEqual(result, False)
        # Confirms balance remained unchanged
        self.assertEqual(self.testObject.getBalance(), 100.0)

    def testWithdrawal(self):
        # Attempts to withdraw a valid amount
        result = self.testObject.withdraw(50.0)
        # Ensures withdrawal was successful
        self.assertEqual(result, True)
        # Ensures the balance was updated correctly
        self.assertEqual(self.testObject.getBalance(), 50.0)

    def testOverdraft(self):
        # Sets balance to 20.0
        self.testObject._balance = 20.0
        # Attempts to withdraw more than the balance to trigger an overdraft
        result = self.testObject.withdraw(50.0)
        # Ensures withdrawal was successful
        self.assertEqual(result, True)
        # Ensures overdraft was applied correctly
        self.assertEqual(self.testObject.getBalance(), -30.0)

    def testOverdrawnCount(self):
        # Confirms initial overdrawn count is 0
        self.assertEqual(self.testObject.getOverdrawnCount(), 0)
        # Triggers an overdraft
        self.testObject.withdraw(150.0)
        # Ensures overdrawn count was updated
        self.assertEqual(self.testObject.getOverdrawnCount(), 1)

    def testMonthlyFee(self):
        # Applies the monthly fee to the account
        self.testObject.applyMonthlyFee()
        # Ensures the fee was correctly applied
        self.assertEqual(self.testObject.getBalance(), 90.0)

if __name__ == '__main__':
    unittest.main()
