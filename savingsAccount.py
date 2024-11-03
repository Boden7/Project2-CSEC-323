from bankAccount import BankAccount
from transaction import Transaction
from AES_CBC import encrypt_AES_CBC, decrypt_AES_CBC
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

    # method to calculate and apply the interest for savings account:
    # Hunter 
    def calcInterest(self):
        assert(self._balance > 0)
        interest_amount = self._balance * BankAccount._intRates['savings']
        transaction = Transaction("interest", interest_amount)
        # add interest to list of transactions
        self._accountTransactions.append(transaction)
        self.writeTransaction(transaction)
        self.deposit(interest_amount)
        return True

    # An accessor/getter method for the number of times the account has been
    # overdrawn
    # @return: The overdrawn counter associated with the Bank Account (integer)
    # Anna
    def getOverdrawnCount(self):
      return self._overdrawnCount

    # Deposits money into the account if the transaction is valid and records the transaction
    # Boden
    #@param amount: the amount to be deposited
    #@require amount > 0
    #@return The success or failure of the deposit
    def deposit(self, amount):
        # Make sure the amount to deposit a float is not negative
        assert(isinstance(amount, float))
        assert(amount > 0)
        # Process the transaction and update necessary variables
        depositTransaction = Transaction("deposit", amount)
        # add deposit to list of transactions
        self._accountTransactions.append(depositTransaction)
        self.writeTransaction(depositTransaction)
        self._balance += amount
        if self.getBalance() >= 100.0:
            self._overdrawnCount = self._overdrawnCount - 1
        if self.getBalance() >= 10000.0:
            # if the account balance exceeds 10000 reset overdrawn counter:
            self._overdrawnCount = 0
        return True

    # Withdrawals money from the account if the transaction is valid and records the transaction; 
    # If the transaction is valid but the account will be overdrawn, applies an overdraft fee and 
    # updates the counter for overdraws
    # Boden
    #@param amount: the amount to be withdrawn
    #@require amount > 0
    #@return The success or failure of the withdrawal
    def withdraw(self, amount):
        # Make sure the amount to withdrawal is not negative
        assert(isinstance(amount, float))
        assert(amount <= 0)
        # Ensure the balance is at least $250 more than the withdrawal amount
        if amount < self.getBalance() + 250.0 and self._overdrawnCount < 3:
            # Process the transaction and update necessary variables
            withdrawalTransaction = Transaction("withdrawal", amount)
            # add withdrawal to list of transactions
            self._accountTransactions.append(withdrawalTransaction)
            self._balance -= amount
            # If the withdrawal would put the balance in the negative, add an
            # overdraft fee and increment the overdrawn counter
            if self.getBalance() < 0.0:
                # Process the transaction and update necessary variables
                self._balance -= self.getOverdraft()
                penaltyTransaction = Transaction("penalty", self.getOverdraft())
                # add penalty to list of transactions
                self._accountTransactions.append(penaltyTransaction)
                self._overdrawnCount = self.getOverdrawnCount() + 1 
                print("The account is overdrawn")
            return True
        # If the overdraw limit is exceeded or the withdraw is not possible return False
        else:
            print("Transaction denied")
        return False

    # Prints all transactions for the savings account
    # Hunter 
    def printTransactionList(self):
        print("Savings Account Transactions:")
        print(super.printTransactionList())

    # Method to write all transactions made on a savings account to the savings.txt
    # file, data is encrypted first
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
    def readTransactions(self):
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
                print("Decrypted transaction:", data.decode())
                infile.readline()  # Skip the newline
                length = infile.readline().rstrip().decode()
