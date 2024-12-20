""" 
This module defines the SavingsAccount class.
@author: Hunter Peacock, Boden Kahn, Brenden Shelton, and Anna Pitt
@date: November 4, 2024

A class to represent the data elements and methods required to implement a SavingsAccount
This class is inherited from the BankAccount superclass
"""

# Import statements
from bankAccount import BankAccount
from transaction import Transaction
from AES_CBC import encrypt_AES_CBC, decrypt_AES_CBC

# Hunter 
class SavingsAccount(BankAccount):
    
    # A private class variable that holds the overdraft fee amounts for savings accounts
    _overdraftFee = [20.00, 30.00, 50.00]

    # Constructs a SavingsAccount object.
    #
    #  @param balanceIn: The starting balance of the Savings Account (Floating point)
    #
    #  @ensure SavingsAccount object successfully created    
    def __init__(self, balanceIn = 0.0):
        super().__init__(balanceIn, account_type = 'savings')
        self._overdrawnCount = 0  # Counter for overdrafts (savings only)

    # An accessor/getter method for the overdraft fee
    #
    # @return: The overdraft fee (floating-point value)
    # Anna
    def getOverdraft(self):
        return self._overdraftFee[self.getOverdrawnCount() - 1]

    # An accessor/getter method for the number of times the account has been
    # overdrawn
    #
    #   @return: The overdrawn counter associated with the Bank Account (integer)
    # Anna
    def getOverdrawnCount(self):
        return self._overdrawnCount
    
    # An mutator/setter method for the number of times the account has been
    # overdrawn
    #
    # Boden
    def _setOverdrawnCount(self, overdrawnCount: int):
        self._overdrawnCount = overdrawnCount

    # Deposits money into the account if the transaction is valid and records the transaction
    #
    #  @param amount: the amount to be deposited
    #
    #  @require amount must be a positive, floating-point value
    #
    #  @return The success or failure of the deposit
    # Boden
    def deposit(self, amount):
        # Make sure the amount to deposit a float is not negative
        assert(isinstance(amount, float))
        assert(amount > 0)
        # Process the transaction and update necessary variables
        depositTransaction = Transaction("deposit", amount)
        # add deposit to list of transactions
        self._accountTransactions.append(depositTransaction)
        self._writeTransaction(depositTransaction)
        self._balance += amount
        if self.getBalance() >= 100.0 and self.getOverdrawnCount() > 0:
            self._setOverdrawnCount (self._overdrawnCount - 1)
        if self.getBalance() >= 10000.0:
            # if the account balance exceeds 10000 reset overdrawn counter:
            self._setOverdrawnCount(0)
        return True

    # Withdraws money from the account if the transaction is valid and records the transaction
    # If the transaction is valid but the account will be overdrawn, applies an overdraft fee and 
    # updates the counter for overdrawn
    #
    #  @param amount: the amount to be withdrawn
    #
    #  @require amount must be a positive, floating-point value
    #
    #  @return The success or failure of the withdrawal
    # Boden
    def withdraw(self, amount):
        # Make sure the amount to withdrawal is not negative
        assert(isinstance(amount, float))
        assert(amount >= 0)
        # Ensure the balance is at least $250 more than the withdrawal amount
        assert amount < self.getBalance() + 250.0 and self.getOverdrawnCount() < 3, "Transaction denied"
        # Process the transaction and update necessary variables
        withdrawalTransaction = Transaction("withdrawal", amount)
        # add withdrawal to list of transactions
        self._accountTransactions.append(withdrawalTransaction)
        self._balance -= amount
        # If the withdrawal would put the balance in the negative, add an
        # overdraft fee and increment the overdrawn counter
        if self.getBalance() < 0.0:
            # Process the transaction and update necessary variables
            self._setOverdrawnCount(self.getOverdrawnCount() + 1)
            self._balance -= self.getOverdraft()
            penaltyTransaction = Transaction("penalty", self.getOverdraft())
            # add penalty to list of transactions
            self._accountTransactions.append(penaltyTransaction)
            print("The account is overdrawn")
        return True

    # Transfer an amount of money from one account to another
    #
    #  @param amount: The amount being transferred to the other account
    #  @param otherAccount: The account that is being transferred the money (if possible)
    #
    #  @return: True if the money was able to be transferred and False if not
    # Boden
    def transfer(self, amount, otherAccount):
        assert self.withdraw(amount)
        otherAccount.deposit(amount)
        transaction = Transaction("transfer", amount)
        # add transfer to list of transactions
        self._accountTransactions.append(transaction)
        self._writeTransaction(transaction)
        return True

    # Calculates the interest payment for a savings account, adds a new interest transaction
    # to the account, and updates the account balance
    #
    #  @require balance > 0
    #
    #  @return if the interest was added or not    
    # Hunter 
    def calcInterest(self):
        assert(self.getBalance() > 0)
        interest_amount = self.getBalance() * BankAccount._intRates['savings']
        transaction = Transaction("interest", interest_amount)
        # add interest to list of transactions
        self._accountTransactions.append(transaction)
        self._writeTransaction(transaction)
        self.deposit(interest_amount)
        return True
    
    # Prints a String representation of all transactions for a Savings Account object      
    # Hunter 
    def printTransactionList(self):
        print("Savings Account Transactions:")
        print(super().printTransactionList())

    # Method to write all transactions made on a savings account to the savings.txt
    # file
    # Data is encrypted first
    #
    #  @param transaction: The transaction to be written to the file
    # Hunter 
    def _writeTransaction(self, transaction: Transaction):
        # Set the Debug Flag
        DEBUG = False
        # Encryption key (Ensure the key is 16, 24, or 32 bytes for AES-128, AES-192, or AES-256)
        key = b'MySuperSecretKey1222222222222222'
        # Initialization vector (Ensure the IV is 16 bytes)
        iv = b'MySuperSecretIV1'

        if DEBUG:
            print("The length of the key is %d bytes" % len(key))
            print("The length of the Initialization Vector is %d bytes" % len(iv))

        # Open the file to write the data
        with open("savings.txt", "wb") as outfile:
            # Convert transaction to string, then encrypt
            transaction_str = str(transaction)
            # Encrypt the transaction data
            encrypted_data = encrypt_AES_CBC(transaction_str, key, iv)
            # Write the length of the encrypted data to the file
            outfile.write(str(len(encrypted_data)).encode())
            outfile.write(b"\n")
            # Write the encrypted data to the file
            outfile.write(encrypted_data)
            outfile.write(b"\n")

        if DEBUG:
            print("Transactions written to savings.txt.")

    # Method to read all transactions made on a checking account to the checking.txt
    # file, data is decrypted first
    # Hunter
    def _readTransactions(self):
        # Set the Debug Flag
        DEBUG = False
        key = b'MySuperSecretKey1222222222222222'
        iv = b'MySuperSecretIV1'

        # Open the file to read the data
        with open("savings.txt", "rb") as infile:
            length = infile.readline().rstrip().decode()

            while length != "":
                length = int(length)
                if DEBUG:
                    print("Length: ", length)
                data = infile.read(length)
                data = decrypt_AES_CBC(data, key, iv)
                # process the decrypted data: 
                print("Decrypted transaction:", data)
                infile.readline()  # Skip the newline
                length = infile.readline().rstrip().decode()

    # repr method to print the information of a clients checking account: 
    def __repr__(self):
        return (f"Account Number: {super().getAccountNumber()}\n"
                f"Balance: {self._balance:.2f}\n"
                f"Account Type: '{super().getAccountType()}'\n"
                f"Overdrawn Count: '{self.getOverdrawnCount()}'\n"
                f"Transactions:\n{super().printTransactionList()}")
