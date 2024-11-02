# Class to store the names of clients:
# Hunter 
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
