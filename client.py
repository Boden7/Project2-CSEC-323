""" 
This module defines the Client class.
@author: Hunter Peacock, Boden Kahn, Brenden Shelton, and Anna Pitt
@date: November 4, 2024

A class to represent the data elements and methods required to implement a Client
"""

# Import statements
from name import Name
from address import Address
from phoneNumber import PhoneNumber
from bankAccount import BankAccount

# Hunter
class Client:
   
   client_counter = 100 # client number set to monotonically increase
   
   # Constructs a Client object.
   #
   #  @param name: The name of the Client (Name)
   #  @param address: The address of the Client (Address)
   #  @param phoneNumber: The phone number of the Client (PhoneNumber)
   #
   #  @ensure Client object successfully created   
   def __init__(self, name: Name, address: Address, phoneNumber: PhoneNumber):
      
      self._clientNumber = Client.client_counter
      Client.client_counter += 1 # monotonically increase client number with each new instance of a client

      self._name = name 
      self._address = address
      self._phoneNumber = phoneNumber
      self._bankAccounts = []

   # Opens a new client bank account
   #
   #  @param account: The new account to be added to the Client (BankAccount)
   #
   #  @require BankAccount object not already stored in the client account     
   def openBankAccount(self, account: BankAccount):
      assert account not in self._bankAccounts, "Account already exists."
      
      # Adds the account to the client's list of accounts
      self._bankAccounts.append(account)

   # Closes a client's already existing bank account
   #
   #  @param account: The account to be deleted from the Client (BankAccount)
   #
   #  @require BankAccount object must already be stored in the client account  
   # Edited by Anna
   def closeBankAccount(self, account: BankAccount): #Update in group file
      assert account in self._bankAccounts, "Account not found."
      assert account.getBalance() > 0, "Cannot close an account with an outstanding balance"
      # withdraw all funds and remove the account: 
      print(f"Withdrawing all funds from account: {account.getAccountNumber()}.")
      
      # Determines how much money is currently being stored within the account
      accountBal = account.getBalance()
      
      # Withdraws the full account balance from the account
      account.withdraw(accountBal)
      
      print(f"Account {account.getAccountNumber()} closed.")
      
      # Removes the account from the list and dereferences it
      self._bankAccounts.remove(account)
      account = None

   # Returns a list of the client's bank accounts
   #
   #  @return: The list associated with the client's bank accounts (List)   
   def getClientAccounts(self):
      return self._bankAccounts
   
   # Returns the client number associated with a particular client
   #
   #  @return: The client number of a particular client (int)  
   def getClientNumber(self):
      return self._clientNumber
   
   # Returns the next available client number
   #
   #  @return: The next available client number (int)  
   def getNextClientNumber(self):
      return Client.client_counter
   
   # Repr method for string representation of a particular client
   #
   #  @return: A String representation of the Client object (String)   
   def __repr__(self): 
      details = (
      f"Client Number: {self.getClientNumber()}\n"
      f"Name: {self._name.__repr__()}\n"
      f"Phone Number: {self._phoneNumber.__repr__()}\n"
      f"Address: {self._address.__repr__()}\n"
      )
      if len(self._bankAccounts) == 0:
         details += f"There are no bank accounts associated with client {self.getClientNumber()}\n"
      else:
         details += "Bank Accounts: \n"
         for account in self._bankAccounts:
            details += (f"{account.__repr__()}\n")
      return(details)

   # Compares two Clients to see if they are the same
   #
   # @param other: The client to compare the original client (self) to
   #
   # @require: other must be a Client instance
   #
   # @return: True if the two Clients are equal, False if not
   # Brenden
   def __eq__(self, other):
      # Check if other is an instance of Client
      assert(isinstance(other, Client)), "Comparison must be between two Client instances."
      
      # Compare immutable variables
      return (self._clientNumber == other._clientNumber)
