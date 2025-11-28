class Dog:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def bark(self):
        return "Bow Wow"

    def info(self):
        return f'Name :{self.name}, Age :{self.age}'