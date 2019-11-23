class Person:

    def __init__(self, name):
        self.name = name
      
    def greet(self, person_name):
        return f"Hello {person_name}, my name is {self.name}"
