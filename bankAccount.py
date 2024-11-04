#  This module defines the BankAccount class.
#  A class to represent the data elements and methods required to implement a bank account.

# Import statements
from transaction import Transaction
from abc import ABC, abstractmethod

class BankAccount:
    # A private class variable that holds the number of the next account value
    _nextAccountVal = 1000

    # A private class variable that holds the overdraft fee amounts for savings accounts
    _overdraftFee = [20.00, 30.00, 50.00]
    
    # A private class variable that holds the interest rates in decimal form 
    _intRates = {'checking': 0.015, 'savings': 0.04}

    # Hunter 
    def __init__(self, balanceIn = 0.0, account_type = 'checking'):
        # Assert statements for preconditions
        assert isinstance(balanceIn, float), "The balance must be a floating-point value."
        assert balanceIn >= 0.0, "The balance must be a positive value." 
        assert account_type in ['checking', 'savings'], "Invalid account type."

        # Sets the instance variables
        self._accountNum = BankAccount._nextAccountVal
        # Updates the next account value
        BankAccount._nextAccountVal += 1
        self._accountTransactions = []  # Container to store all transactions on an account
        self._balance = balanceIn
        self._overdrawnCount = 0  # Counter for overdrafts (savings only)
        self._accountType = account_type

    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
     
    @abstractmethod
    def transfer(self, amount, otherAccount):
        pass

    # Accessor/getter to retrieve the balance of an account: 
    # Anna 
    def getBalance(self):
        return self._balance

    # Accessor/getter to retrieve the account number: 
    # Anna 
    def getAccountNumber(self):
        return self._accountNum

    # Accessor/getter to retrieve the next account number:
    # Hunter 
    def getNextAccountNumber(self):
      # returns the next available account number:
      return BankAccount._nextAccountVal

    # Returns a String representation of the transactions for a Bank Account object
    #
    # @return: A String representation of the transactions stored within a Bank Account object (String)
    # Anna
    def printTransactionList(self):
      # If the transaction list is empty
      if(len(self._accountTransactions) == 0):
         return("There are no valid transactions to display.")
      
      # If there is at least one transaction in the transaction list to display
      else:
         # Creates a String variable to hold the list of transactions
         transList = ""
         
         # Loops through every transaction in the list
         for transIndex in range(len(self._accountTransactions)):
            
            # If the transaction is the last one in the list
            if(transIndex == (len(self._accountTransactions) - 1)):
               # Adds the String representation of the transaction to transList (without a new line)
               transList = transList + str(self._accountTransactions[transIndex])
               
            # If the transaction is not the last one in the list
            else:
               # Adds the String representation of the transaction to transList (with a new line)
               transList = transList + str(self._accountTransactions[transIndex]) + "\n"
      
      # Returns the full amount of transactions as a String
      return(transList)
   
    @abstractmethod
    def _writeTransaction(self):
        pass

    @abstractmethod
    def _readTransactions(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    # method that checks for equality between accounts 
    # Hunter 
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return (self._accountNum == other._accountNum and
                self._balance == other._balance and
                self._accountType == other._accountType)
