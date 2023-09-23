"""
This is the NoneRecord class definition
written by : Joe Defendre 
version: 1.0
copyright 2023
"""

class NameRecord:
    """ 
    this is the NameRecord class definition
    """
    def __init__(self, first_name: str, last_name: str):
        """ 
        this is the constructor
        """
        self.first_name = None
        self.last_name = None 
        
    def get_first_name(self):
        """ 
        this is the get_first_name method
        """
        return self.first_name
    def set_first_name(self, first_name: str):
        """ 
        this is the set_first_name method
        """
        self.first_name = first_name
    def get_last_name(self):
        """ 
        this is the get_last_name method
        """
        return self.last_name
    def set_last_name(self, last_name: str):
        """ 
        this is the set_last_name method
        """
        self.last_name = last_name
