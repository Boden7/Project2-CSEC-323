from name import Name
from address import Address
from phoneNumber import PhoneNumber
from bankAccount import BankAccount

class Client: # Hunter 
   
   client_counter = 100 # client number set to monotonically increase
   
   def __init__(self, name: Name, address: Address, phoneNumber: PhoneNumber):
      
      self._clientNumber = Client.client_counter
      Client.client_counter += 1 # monotonically increase client number with each new instance of a client

      self._name = name 
      self._address = address
      self._phoneNumber = phoneNumber
      self._bankAccounts = []

   # open a bank account:
   def openBankAccount(self, account: BankAccount):
     assert account not in self._bankAccounts, "Account already exists."
     # add the account to the clients list of accounts:
     self._bankAccounts.append(account)

   # close a bank account:
   def closeBankAccount(self, account):
     assert account in self._bankAccounts, "Account not found."
     # withdraw all funds and remove the account: 
     print(f"Withdrawing all funds from account: {account}.")
     print(f"Account {account} closed.")
     # remove the account from the list and dereference it
     self._bankAccounts.remove(account)
     account = None

   def getClientAccounts(self):
      # returns a list of the clients bank accounts:
      return self._bankAccounts
   
   def getClientNumber(self):
      # returns the clients account number:
      return self._clientNumber
   
   def getNextClientNumber(self):
      # returns the next available client number:
      return Client.client_counter
   
   # repr method for client class: 
   def __repr__(self): 

     details = (
     f"Client Number: {self._clientNumber}\n"
     f"Name: {self._name}\n"
     f"Phone Number: {self._phoneNumber}\n"
     f"Address: {self._address}\n"
     f"Bank Accounts: {self._bankAccounts}\n"
     )
     print(details)
