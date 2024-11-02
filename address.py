# Class containing address information for clients 
# Hunter 
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

    # repr method for string representation of the full address:
    # Hunter 
    def __repr__(self):
      return f"{self._street}, {self._city}, {self._state}"
