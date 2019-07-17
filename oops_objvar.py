class Person:
    """Represents the person class"""

    population = 0

    def __init__(self, name):
        """initializes the data"""
        self.name = name
        Person.population += 1
        print("Person Instantiated.{}".format(self.name))

    def say_hi(self, myname=None):
        if not myname:
            print("Hello {}!".format(self.name))
        else:
            print("Hello {}!".format(myname))
    
    def die(self):
        Person.population -= 1

    @classmethod
    def how_many(cls):
        print("This class has now {} instances.".format(cls.population))
        return cls.population


p = Person("Atul")
p.how_many()
p.say_hi()
q = Person("1")
p.how_many()

