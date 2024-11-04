""" 
This module defines the a tester for the PhoneNumber class.
@author: Anna Pitt
@date: November 3, 2024

Import the unittest module and the PhoneNumber module
Test each method with at least one unit test
"""

import unittest
from unittest.mock import patch
from PhoneNumber import PhoneNumber

class TestPhoneNumber(unittest.TestCase):
    # Tests not done in this tester that have been tested elsewhere:
    # - Valid constructor for a PhoneNumber (tested in Client tester and setUp)
    # - Call to getPhoneNumber() (tested in Client tester)
    # - Valid call to setPhoneNumber() (tested in Client tester)
    # - Call to repr (tested in Client's repr in Client tester)
    
    # Anna
    def setUp(self):
        # Initializes incorrect phone numbers
        self.invalidLength = "804000000"
        self.invalidChars = "804-000-0000"
        self.invalidInstance = 8040000000
        self.invalidIndex = "0000000000"
        self.invalidEmpty = ""
        
        # Initializes a valid phone number to attempt to change
        self.validNum = PhoneNumber("8040000000")
    
    def test_ConstructorInvalidLength(self):
        print("\nTesting the constructor with an invalid phone number length of 9")
        
        # Ensures the PhoneNumber object with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, PhoneNumber, self.invalidLength)
    
    def test_ConstructorInvalidLengthEmpty(self):
        print("\nTesting the constructor with an invalid phone number length of 0 (empty string)")
        
        # Ensures the PhoneNumber object with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, PhoneNumber, self.invalidEmpty)
    
    def test_ConstructorInvalidCharacters(self):
        print("\nTesting the constructor with an invalid phone number with non-digit characters")
        
        # Ensures the PhoneNumber object with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, PhoneNumber, self.invalidChars) 
    
    def test_ConstructorInvalidInstance(self):
        print("\nTesting the constructor with an invalid phone number type")
        
        # Ensures the PhoneNumber object with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, PhoneNumber, self.invalidInstance)
    
    def test_ConstructorInvalidFirstIndex(self):
        print("\nTesting the constructor with an invalid first index of the phone number")
        
        # Ensures the PhoneNumber object with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, PhoneNumber, self.invalidIndex)
    
    def test_setPhoneNumberInvalidLength(self):
        print("\nTesting setPhoneNumber() with an invalid phone number length of 9")
        
        # Ensures the call to setPhoneNumber() with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, self.validNum.setPhoneNumber, self.invalidLength)
    
    def test_setPhoneNumberInvalidLengthEmpty(self):
        print("\nTesting setPhoneNumber() with an invalid phone number length of 0 (empty string)")
        
        # Ensures the call to setPhoneNumber() with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, self.validNum.setPhoneNumber, self.invalidEmpty)
    
    def test_setPhoneNumberInvalidCharacters(self):
        print("\nTesting setPhoneNumber() with an invalid phone number with non-digit characters")
        
        # Ensures the call to setPhoneNumber() with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, self.validNum.setPhoneNumber, self.invalidChars) 
    
    def test_setPhoneNumberInvalidInstance(self):
        print("\nTesting setPhoneNumber() with an invalid phone number type")
        
        # Ensures the call to setPhoneNumber() with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, self.validNum.setPhoneNumber, self.invalidInstance)
    
    def test_setPhoneNumberInvalidFirstIndex(self):
        print("\nTesting setPhoneNumber() with an invalid first index of the phone number")
        
        # Ensures the call to setPhoneNumber() with false call to phone number parameter
        # throws an assertion error
        self.assertRaises(AssertionError, self.validNum.setPhoneNumber, self.invalidIndex)       

if __name__ == '__main__':
    unittest.main()
