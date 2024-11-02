from bankAccount import BankAccount
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
    def printTransactionList(self):
        print("Checking Account Transactions:")
        super().transactionList()


    # Method to write all transactions made on a checking account to the checking.txt
    # file, data is encrypted first
    # Hunter
    def _write_transactions(self):
        with open('checking.txt', 'w') as file:
            # encrypted_data = 
            file.write(encrypted_data)

    # Method to read all transactions made on a checking account to the checking.txt
    # file, data is decrypted first
    # Hunter
    def _read_transactions(self):
        with open('checking.txt', 'r') as file:
            encrypted_data = file.read()
          # decrypted_data = 
          # transactions = 
            for transaction in transactions:
                print(transaction)
                
   
