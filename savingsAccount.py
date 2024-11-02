from bankAccount import BankAccount
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
    def printTransactionList(self):
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
