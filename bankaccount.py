#  This module defines the BankAccount class.
#  A class to represent the data elements and methods required to implement a bank account.

# Import statements
from transaction import Transaction
from datetime import datetime


class Name: 
      
    def __init__(self, first_name: str, last_name: str):
      # Assert statements for preconditions
      assert first_name.isalpha(), "The first name must not contain any special characters."
      assert len(first_name) > 0 and len(first_name) <= 25, "The first name must be a valid length."
      assert last_name.isalpha(), "The last name must not contain any special characters."
      assert len(last_name) > 0 and len(last_name) <= 40, "The last name must be a valid length."
      
      self._firstName = first_name 
      self._lastName = last_name 

    def __str__(self):
      return f"{self._firstName} {self._lastName}"
    
    # An accessor/getter method for the first name
    #
    # @return: The first name associated with the Bank Account (String)
    # Anna
    def getFirst(self):
      return self._firstName
   
    # An accessor/getter method for the last name
    #
    # @return: The last name associated with the Bank Account (String)
    # Anna
    def getLast(self):
      return self._lastName

    # A mutator/setter method for the last name
    # @param last: The new last name for the Bank Account (String: default is an empty string)
    # @require: last is between 1 and 40 characters inclusive and has no special characters   
    # Anna
    def setLast(self, last):
      # Assert statements for preconditions
      assert last.isalpha(), "The last name must not contain any special characters."
      assert len(last) > 0 and len(last) <= 40, "The last name must be a valid length."
      
      self._lastName = last

    # A mutator/setter method for the first name
    # @param first: The new first name for the Bank Account (String: default is an empty string)
    # @require: first is between 1 and 25 characters inclusive and has no special characters   
    # Anna
    def setFirst(self, first):
      # Assert statements for preconditions
      assert first.isalpha(), "The first name must not contain any special characters."
      assert len(first) > 0 and len(first) <= 25, "The first name must be a valid length."      
      
      self._firstName = first
      
class PhoneNumber: 
    
    def __init__(self, phoneNum: str):
      assert isinstance(phoneNum, str), "The phone number must be a string composed of integer values."
      assert phoneNum.isdigit(), "The phone number must only contain integer values."
      assert len(phoneNum) == 10, "The phone number must be ten characters in length."
      assert phoneNum[0] != '0', "The phone number cannot start with '0'."
      
      self._phoneNum = phoneNum

   # Accessor/getter method for the phone number
   def getPhoneNumber(self):
      return self._phoneNum

   # Mutator/setter method for the phone number
   def setPhoneNumber(self, number: str):
      # Sets a new phone number after validating it:
      # Ensures new phone number is valid
      assert isinstance(number, str), "The phone number must be a string composed of integer values."
      assert number.isdigit(), "The phone number must only contain integer values."
      assert len(number) == 10, "The phone number must be ten characters in length."
      assert number[0] != '0', "The phone number cannot start with '0'."
      
      self._phoneNum = number # ensures most current value is set (updates phone number)


    def __str__(self):
      return f"+1({self._phoneNum[0,1,2]}){self._phoneNum[3,4,5]}-{self._phoneNum[6,7,8,9]}"
      
class Address:
    
    def __init__(self, street: str, city: str, state: str):

      assert street.isalpha(), "The street must not contain any special characters."
      assert len(street) > 0 and len(street) <= 30, "The street must be a valid length."
     
      assert city.isalpha(), "The city must not contain any special characters."
      assert len(city) > 0 and len(city) <= 30, "The city must be a valid length."
      
      assert state.isalpha(), "The state must not contain any special characters."
      assert len(state) == 2, "State abbreviation must be two characters in length."
      assert state in ["VA", "MD", "NJ", "PA", "DE", "NC", "WV", "DC"], "Invalid State designated."
      
      self._street = street
      self._city = city
      self._state = state 

    # Accessor/getter for the street name
    # Hunter 
    def getStreet(self):
        return self._street

    # Accessor/getter for the city name
    # Hunter 
    def getCity(self):
        return self._city

    # Accessor/getter for the state abbreviation
    # Hunter 
    def getState(self):
        return self._state

    # Mutator/setter for the street
    # Hunter 
    def setStreet(self, street: str):
        assert street.isalpha(), "The street must not contain any special characters."
        assert len(street) > 0 and len(street) <= 30, "The street must be a valid length."
        self._street = street

    # Mutator/setter for the city
    # Hunter
    def setCity(self, city: str):
        assert city.isalpha(), "The city must not contain any special characters."
        assert len(city) > 0 and len(city) <= 30, "The city must be a valid length."
        self._city = city

    # Mutator/setter for the state
    # Hunter 
    def setState(self, state: str):
        assert state.isalpha(), "The state must not contain any special characters."
        assert len(state) == 2, "State abbreviation must be two characters in length."
        assert state in ["VA", "MD", "NJ", "PA", "DE", "NC", "WV", "DC"], "Invalid state designated."
        self._state = state

    # repr for full address:
    # Hunter 
    def __str__(self):
      return f"{self._street}, {self._city}, {self._state}"

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
   def open_bank_account(self, account):
     assert account not in self._bankAccounts, "Account already exists."
     # add the account to the clients list of accounts:
     self._bankAccounts.append(account)

   # close a bank account:
   def close_bank_account(self, account):
     assert account in self._bankAccounts, "Account not found."
     # withdraw all funds and remove the account: 
     print(f"Withdrawing all funds from account: {account}.")
     print(f"Account {account} closed.")
     self._bankAccounts.remove(account)

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
   def display_details(self): 

     details = (
     f"Client Number: {self._clientNumber}\n"
     f"Name: {self._name}\n"
     f"Phone Number: {self._phoneNumber}\n"
     f"Address: {self._address}\n"
     f"Bank Accounts: {self._bankAccounts}\n"
     )
     print(details)

class BankAccount:
    # A private class variable that holds the number of the next account value
    _nextAccountVal = 1000

    # A private class variable that holds the overdraft fee amounts for savings accounts
    _overdraftFee = [20.00, 30.00, 50.00]
    
    # A private class variable that holds the interest rates in decimal form 
    # (checking cannot be overdrafted)
    _intRates = {'checking': 0.015, 'savings': 0.04}

    # Hunter 
    def __init__(self, balanceIn = 0.0, account_type = 'checking'):
        # Assert statements for preconditions
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
        


    # Deposits money into the account if the transaction is valid and records the transaction
    # Boden
    #@param amount: the amount to be deposited
    #@require amount > 0
    #@return The valid or failure of the deposit
    def deposit(self, amount):
       # Make sure the amount to deposit is not negative
       if isinstance(amount, float) and amount > 0:
           # Process the transaction and update necessary variables
           depositTransaction = Transaction("deposit", amount)
           # Add deposit to list of transactions
           self._accountTransactions.append(depositTransaction)
           self._balance += amount
           return True
       # If anything was wrong with the amount parameter the transaction will be rejected
       return False
    
    # Hunter 
    #@param amount: the amount to be withdrawn
    #@require amount > 0
    #@return The valid or failure of the withdrawal
    def withdraw(self, amount):
        # ensure amount to withdraw is not negative
        if isinstance(amount, float) and amount > 0:
            # if there are enough funds to withdraw from the account: 
            if self._balance >= amount:
                transaction = Transaction("withdrawal", amount)
                self._accountTransactions.append(transaction)
                # deduct amount from the balance of the account
                self._balance -= amount 
                return True
            print("Withdrawal denied: insufficient funds.")
        return False
 
     
    # Transfer an amount of money from one account to another
    # cannot transfer funds between the same account.
    # @param amount: The amount being transferred to the other account
    # @param otherAccount: The account that is being transferred the money (if possible)
    # @return: True if the money was able to be transferred and False if not
    # Brenden - updated by Hunter for P2:
    def transfer(self, amount, otherAccount):
        if isinstance(otherAccount, BankAccount) and otherAccount != self:
            if self.withdraw(amount):
                otherAccount.deposit(amount)
                transaction = Transaction("transfer", amount)
                self._accountTransactions.append(transaction)
                return True
        return False

    # Accessor/getter to retrieve the balance of an account: 
    # Anna 
    def getBalance(self):
        return self._balance

    # Accessor/getter to retrieve the account number: 
    # Anna 
    def getAccountNumber(self):
        return self._accountNum

   
    # Returns a String representation of the transactions for a Bank Account object
    #
    # @return: A String representation of the transactions stored within a Bank Account object (String)
    # Anna
    def transactionList(self):
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
   

    def _write_transactions(self, filename):
        with open(filename, 'w') as file:
           # encrypted_data = 
            file.write(encrypted_data)

    def _read_transactions(self, filename):
        with open(filename, 'r') as file:
            encrypted_data = file.read()
          # decrypted_data = 
          # transactions = 
            for transaction in transactions:
                print(transaction)

    def _encrypt_data(self, data):
      # encoded_bytes = 
        return encoded_bytes.decode('utf-8')

    def _decrypt_data(self, data):
      # decoded_bytes = 
        return decoded_bytes.decode('utf-8')


    # Returns a String representation of a Bank Account object
    #
    # @return: A String representation of the Bank Account object (String)
    # Anna - edited by Hunter for P2
    def __repr__(self):
      # Creating the list of valid transactions to print to the screen
      transactionVals = self.transactionList()
      
      return ("%s Account #%d owned by %s %s has a balance of %.2f. The valid transactions include:\n%s" % \
         (self._accountType.capitalize(), self._accountNum, self._firstName, self._lastName, self._balance, transactionVals))

# Class representing a checking account 
# Inherited from the BankAccount superclass
# Hunter 
class CheckingAccount(BankAccount):

    def __init__(self, balanceIn = 0.0):
        super().__init__(balanceIn, account_type = 'checking')

    # Method to withdraw an amount from a checking account 
    # Hunter 
    def withdraw(self, amount):
        if isinstance(amount, float) and amount > 0:
            if self._balance >= amount:
                return super().withdraw(amount)
            else:
                print("Withdrawal denied: insufficient funds.")
        return False

    # Method to calculate and apply the interest for checking account:
    # Hunter
    def calc_interest(self):
        if self._balance > 0:
            interest_amount = self._balance * BankAccount._intRates['checking']
            self.deposit(interest_amount)
            return True
        return False
    
    # Prints all transactions of a checking account
    # Hunter 
    def print_transactions(self):
        print("Checking Account Transactions:")
        super().transactionList()

    # Method to write all transactions made on a checking account to the checking.txt
    # file, data is encrypted first
    # Hunter
    def write_transactions(self):
        super()._write_transactions("checking.txt")

    # Method to read all transactions made on a checking account to the checking.txt
    # file, data is decrypted first
    # Hunter
    def read_transactions(self):
        super()._read_transactions("checking.txt")


# class to represent a savings account
# inheriting from BankAccount superclass
# Hunter 
class SavingsAccount(BankAccount): 
    def __init__(self, balanceIn = 0.0):
        super().__init__(balanceIn, account_type = 'savings')

    # An accessor/getter method for the overdraft fee
    #
    # @return: The overdraft fee (floating-point value)
    # Anna
    def getOverdraft(self):
      return BankAccount._overdraftFee


    # An accessor/getter method for the number of times the account has been
    # overdrawn
    # @return: The overdrawn counter associated with the Bank Account (integer)
    # Anna
    def getOverdrawnCount(self):
      return self._overdrawnCount

    # method to withdraw an amount from savings account
    # Hunter 
    def withdraw(self, amount):
        assert isinstance(amount, float), "Amount must be valid."
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if self._overdrawnCount < 3:
            if self._balance >= amount:
                valid = super().withdraw(amount)
                # if the account balance exceeds 10000 reset overdrawn counter:
                if valid and self._balance >= 10000:
                    self._overdrawnCount = 0
                return valid
            else:
                self._overdrawnCount += 1
                # overdrawn count check to apply the appropriate fee to the account
                fee = BankAccount._overdraftFee[self._overdrawnCount - 1]
                self._balance -= fee  # Apply overdraft fee to account and update balance
                # information about the overdraft and fee applied
                print(f"Withdrawal denied: insufficient funds. Overdrawn count: {self._overdrawnCount}. Fee applied: {fee:.2f}")
        else:
            print("Withdrawal denied: overdraft limit exceeded.")
        return False

    # Prints all transactions for the savings account
    # Hunter 
    def print_transactions(self):
        print("Savings Account Transactions:")
        print(self.transactionList())

    # Method to write all transactions made on a savings account to the savings.txt
    # file, data is encrypted first
    # Hunter 
    def write_transactions(self):
        super()._write_transactions("savings.txt")

    # Method to read transactions from the savings.txt file
    # data is decrypted first
    # Hunter 
    def read_transactions(self):
        super()._read_transactions("savings.txt")

    # method to calculate and apply the interest for savings account:
    # Hunter 
    def calc_interest(self):
        if self._balance > 0:
            interest_amount = self._balance * BankAccount._intRates['savings']
            self.deposit(interest_amount)
            return True
        return False
