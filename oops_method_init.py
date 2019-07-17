class Person:
        def __init__(self):
            print("Person class instantiated.")

        def say_hi(self, name="atul", lastname=None):
                if not lastname:
                    print("Hello {firstname}!  this is a sample method.".format(firstname=name, lastname=lastname))
                else: 
                    print("Hello {firstname} {lastname}! this is a sample method.".format(firstname=name, lastname=lastname))

p = Person()
p.say_hi("Atul")
p.say_hi("Atul", "Bagga")