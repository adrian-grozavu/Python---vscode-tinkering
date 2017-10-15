"""
    Demonstrating OOP features in Python: encapsulation
"""
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age
    
    # public method
    def show_age(self):
        return self._get_age()

    # non-public method. Can only be used inside our class definition
    def _get_age(self):
        return self._age

ag = Person('AG', 26)
print(ag.show_age())