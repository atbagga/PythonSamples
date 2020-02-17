import pickle

class Administator(object):
    def __init__(self, name):
        self.adminname = name

n1 = input("Enter your name: ")
u1 = Administator(n1)

serialized = pickle.dumps(u1)
filename = 'serialized.corrupt'

with open(filename, 'wb') as fobj:
    fobj.write(serialized)
    fobj.flush()
    fobj.close()
