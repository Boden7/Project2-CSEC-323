from bankAccount import BankAccount
from transaction import Transaction
from AES_CBC import encrypt_AES_CBC, decrypt_AES_CBC
# Class representing a checking account 
# Inherited from the BankAccount superclass
# Hunter 
class CheckingAccount(BankAccount):

    def __init__(self, balanceIn = 0.0):
        super().__init__(balanceIn, account_type = 'checking')

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
        return True

    # Withdrawals money from the account if the transaction is valid and records the transaction; 
    # If the transaction is valid but the account will be overdrawn, applies an overdraft fee and 
    # updates the counter for overdraws
    # Boden
    #@param amount: the amount to be withdrawn
    #@require amount > 0
    #@return The success or failure of the withdrawal
    def withdraw(self, amount):
        assert(isinstance(amount, float))
        assert(amount > 0)
        if self._balance >= amount:
            # Process the transaction and update necessary variables
            withdrawalTransaction = Transaction("withdrawal", amount)
            # add withdrawal to list of transactions
            self._accountTransactions.append(withdrawalTransaction)
            self._writeTransaction(withdrawalTransaction)
            self._balance -= amount
            return True
        else:
            print("Withdrawal denied: insufficient funds.")
            return False

    # Method to calculate and apply the interest for checking account:
    # Hunter
    def calcInterest(self):
        assert(self._balance > 0)
        interest_amount = self._balance * BankAccount._intRates['checking']
        transaction = Transaction("interest", interest_amount)
        # add interest to list of transactions
        self._accountTransactions.append(transaction)
        self._writeTransaction(transaction)
        self.deposit(interest_amount)
        return True
    
    # Prints all transactions of a checking account
    # Hunter 
    def printTransactionList(self):
        print("Checking Account Transactions:")
        print(super().printTransactionList())

    # Method to write all transactions made on a checking account to the checking.txt
    # file, data is encrypted first
    # Hunter, fixed by Boden
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
        with open("checking.txt", "wb") as outfile:
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
            print("Transactions written to checking.txt.")

    # Method to read all transactions made on a checking account to the checking.txt
    # file, data is decrypted first
    # Hunter
    def readTransactions(self):
        # Set the Debug Flag
        DEBUG = False
        key = b'MySuperSecretKey1222222222222222'
        iv = b'MySuperSecretIV1'

        # Open the file to read the data
        with open("checking.txt", "rb") as infile:
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
