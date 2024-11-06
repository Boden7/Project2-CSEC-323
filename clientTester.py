""" 
This module defines the tester for the Client class.
@author: Anna Pitt
@date: October 6, 2024

Import the unittest module and the Client module
Test each method with at least one unit test
"""

# Import statements
import unittest
from unittest.mock import patch
from client import Client
from name import Name
from address import Address
from phoneNumber import PhoneNumber

class TestClient(unittest.TestCase):
    # The setup method initializes a client to be used for
    # testing purposes
    # Anna
    def setUp(self):
        # Resets the client counter for each test
        Client.client_counter = 100
        
        # Initializes a valid name, address, and phone number for the client tester
        validName = Name("First", "Last")
        validAddress = Address("100 Street", "City", "VA")
        validPhone = PhoneNumber("8041234567")
        
        # Initializes two valid clients
        self.client1 = Client(validName, validAddress, validPhone)
        self.client2 = Client(validName, validAddress, validPhone)
    
    def test_ConstructorSetFirstName(self):
        print("\nTesting to ensure the constructor can properly set the first name") 
        
        self.client1.setFirstName("OtherFirst")
        
        checkFirst = self.client1.getFirstName()
        
        # Ensures the Client object can properly pull out the renamed first name      
        self.assertEqual(checkFirst, "OtherFirst")
    
    def test_ConstructorSetLastName(self):
        print("\nTesting to ensure the constructor can properly set the last name")
        
        self.client1.setLastName("OtherLast")
        
        checkLast = self.client1.getLastName()
        
        # Ensures the Client object can properly pull out the renamed last name      
        self.assertEqual(checkLast, "OtherLast")
    
    def test_ConstructorSetStreet(self):
        print("\nTesting to ensure the constructor can properly set the street") 
        
        self.client1.setStreet("100 Other Street")
        
        checkStreet = self.client1.getStreet()
        
        # Ensures the Client object can properly pull out the renamed street    
        self.assertEqual(checkStreet, "100 Other Street")
    
    def test_ConstructorSetCity(self):
        print("\nTesting to ensure the constructor can properly set the city")
        
        self.client1.setCity("OtherCity")
        
        checkCity = self.client1.getCity()
        
        # Ensures the Client object can properly pull out the renamed street    
        self.assertEqual(checkCity, "OtherCity")
    
    def test_ConstructorSetState(self):
        print("\nTesting to ensure the constructor can properly set the state") 
        
        self.client1.setState("MD")
        
        checkState = self.client1.getState()
        
        # Ensures the Client object can properly pull out the changed state    
        self.assertEqual(checkState, "MD")
    
    def test_ConstructorSetPhoneNumber(self):
        print("\nTesting to ensure the constructor can properly set the phone number") 
        
        self.client1.setPhoneNumber("8049876543")
        
        checkPhone = self.client1.getPhoneNumber()
        
        # Ensures the Client object can properly pull out the changed phone number    
        self.assertEqual(checkPhone, "8049876543")    
    
    def test_ConstructorGetClientNumber(self):
        print("\nTesting to ensure the constructor can properly get the client number") 
        
        checkClientNum = self.client1.getClientNumber()
        
        # Ensures the Client object can properly pull out the client number   
        self.assertEqual(checkClientNum, 100)
    
    def test_ConstructorGetNextClientNumber(self):
        print("\nTesting to ensure the constructor can properly get the next available client number") 
        
        checkClientNum = self.client1.getNextClientNumber()
        
        # Ensures the Client object can properly pull out the next available client number   
        self.assertEqual(checkClientNum, 101)
    
    def test_ConstructorGetClientAccountsEmpty(self):
        print("\nTesting to ensure the constructor can properly get the list of accounts when the list is empty") 
        
        checkClientAccounts = self.client1.getClientAccounts()
        
        # Ensures the Client object can properly pull out the next available client number   
        self.assertEqual(checkClientAccounts, [])
    
    def test_ConstructorGetClientAccounts(self):
        print("\nTesting to ensure the constructor can properly get the list of accounts when the list is non-empty") 
        
        # ** ADD TRANSACTION HERE
        
        checkClientAccounts = self.client1.getClientAccounts()
        
        # Ensures the Client object can properly pull out the next available client number 
        # ** ADD PROPER CHECK HERE
        self.assertEqual(checkClientAccounts, [])
    
    def test_ConstructorReprEmpty(self):
        print("\nTesting to ensure the constructor can properly list the info of an empty client") 
        
        checkRepr = str(self.client1)
        
        # ** FIX COMPARISON
        compareStr = "- Client Number: 100\n- Name: First Last\n- Phone Number: +1(804)123-4567\n- Address: 100 Street, City, VA\n- Bank Accounts:\n"
        
        # Ensures the Client object can properly represent the client as a string
        self.assertEqual(checkRepr, compareStr)
    
    def test_ConstructorRepr(self):
        print("\nTesting to ensure the constructor can properly list the info of a client with at least one bank account") 
        
        # ** ADD TRANSACTION
        
        checkRepr = str(self.client1)
        
        # ** FIX COMPARISON
        compareStr = "- Client Number: 100\n- Name: First Last\n- Phone Number: +1(804)123-4567\n- Address: 100 Street, City, VA\n- Bank Accounts:\n"
        
        # Ensures the Client object can properly represent the client as a string
        self.assertEqual(checkRepr, compareStr)    
    
    def test_EqualityTrue(self):
        print("\nTesting to ensure that equality works when two clients are equal") 
                
        # Ensures the Client object can properly determine equality  
        self.assertEqual(self.client1, self.client1)
    
    def test_EqualityFalse(self):
        print("\nTesting to ensure that equality works when two clients are not equal") 
                
        # Ensures the Client object can properly determine inequality   
        self.assertNotEqual(self.client1, self.client2)
    
    def test_openBankAccount(self):
        # ** TO BE IMPLEMENTED
        pass
    
    def test_closeBankAccount(self):
        # ** TO BE IMPLEMENTED
        pass    

if __name__ == '__main__':
    unittest.main()
