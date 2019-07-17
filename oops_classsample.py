class Person:
    def __init__(self, msg):
        print("message %s is received", msg)

    def foobar(self):
        print("foobar is called.")


q = Person("q message")
p = Person.foobar(Person("random"))

print (p)

p.foobar()