# Class containing the phone numbers of clients 
# Hunter 
class PhoneNumber: 
    
    def __init__(self, phoneNum: str):
        assert isinstance(phoneNum, str), "The phone number must be a string composed of integer values."
        assert phoneNum.isdigit(), "The phone number must only contain integer values."
        assert len(phoneNum) == 10, "The phone number must be ten characters in length."
        assert phoneNum[0] != '0', "The phone number cannot start with '0'."
      
        self._phoneNum = phoneNum

   # Accessor/getter method for the phone number
   # Hunter 
    def getPhoneNumber(self):
        return self._phoneNum

    # Mutator/setter method for the phone number
    # Hunter 
    def setPhoneNumber(self, number: str):
        # Sets a new phone number after validating it:
        # Ensures new phone number is valid
        assert isinstance(number, str), "The phone number must be a string composed of integer values."
        assert number.isdigit(), "The phone number must only contain integer values."
        assert len(number) == 10, "The phone number must be ten characters in length."
        assert number[0] != '0', "The phone number cannot start with '0'."
      
        self._phoneNum = number # ensures most current value is set (updates phone number)

    # repr method for string representation of the clients phone number 
    def __repr__(self):
        return f"+1({self._phoneNum[0:2]}){self._phoneNum[3:5]}-{self._phoneNum[6:9]}"
