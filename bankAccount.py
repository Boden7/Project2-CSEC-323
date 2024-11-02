#  This module defines the BankAccount class.
#  A class to represent the data elements and methods required to implement a bank account.

# Import statements
from transaction import Transaction

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
    #@return The success or failure of the deposit
    def deposit(self, amount):
        # Make sure the amount to deposit is an int and not negative
        assert(isinstance(amount, float))
        assert(amount > 0)
        # Process the transaction and update necessary variables
        depositTransaction = Transaction("deposit", amount)
        # Add deposit to list of transactions
        self._accountTransactions.append(depositTransaction)
        self._balance += amount
        return True
    
    # Boden
    #@param amount: the amount to be withdrawn
    #@require amount > 0
    #@return The valid or failure of the withdrawal
    def withdraw(self, amount):
        # Make sure the amount to deposit is an int and not negative
        assert(isinstance(amount, float))
        assert(amount > 0)
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
      
        return (f"{self._accountType.capitalize()} Account #{self._accountNum} \
            has a balance of {self._balance:.2f}. Transactions:{transactionVals}")




