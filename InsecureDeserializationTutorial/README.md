## What is Serialisation/Deserialisation?

> Serialisation is the process of converting a data object into a byte stream which can be stored, transmitted and later used to reconstruct the original object. Reconstruction of object is known as deserialisation. 

All modern applications use data serialisation so extensively since the data is passed on the network all the time, objects are cached on the servers, or persisted in the database. The bytes stream is later used to reconstruct the original object to make sense of the data.
Serialising/Deserialising trusted or known data (within the system boundary) is not a concern, but when the data is coming from untrusted sources like user input, it suddenly becomes prone to abuse.

## What is insecure deserialisation?
When a system tries to deserialise data from an untrusted source without appropriate measures it can be used to carry out attacks like denial or service (DOS), abuse application logic or even execute arbitrary code. This is called insecure or untrusted deserialisation.
Insecure Deserialisation is amongst the OWASP top 10 vulnerabilities list in last 3 years.

## Sample code

Serialisation 
```python
import pickle

class User(object):
    def __init__(self, name):
        self.name = name

n1 = input("Enter your name: ")
u1 = User(n1)

serialized = pickle.dumps(u1)
filename = 'serialized.user'

with open(filename, 'wb') as fobj:
    fobj.write(serialized)
    fobj.flush()
    fobj.close()
```

Deserialisation

```python
import pickle

class User(object):
    def __init__(self, name):
        self.name = name

filename = input('Enter filename to deserialize: ')
if not filename:
    filename = 'serialized.user'

with open(filename, 'rb') as fobj:
    raw_data = fobj.read()

deserialized = pickle.loads(raw_data)
print(deserialized.name)
```

What happens if the serialise.user is replaced by a corrupt file. e.g. [serialized.corrupt](https://github.com/atbagga/PythonSamples/blob/master/InsecureDeserializationTutorial/PythonPickleSample/serialized.corrupt)?

What happens if the serialise.user is replaced by a exploit file. e.g. [serialized.hack](https://github.com/atbagga/PythonSamples/blob/master/InsecureDeserializationTutorial/PythonPickleSample/serialized.hack)

Try out the [samples](https://github.com/atbagga/PythonSamples/tree/master/InsecureDeserializationTutorial) and find out. The sample [exploit](https://github.com/atbagga/PythonSamples/blob/master/InsecureDeserializationTutorial/PythonPickleSample/hackSerialize.py) will only create an empty file in your working directory. But the same can be used by an attacker to run any malicious code.

Even [official documentation for pickle](https://docs.python.org/3/library/pickle.html) highlights this security concern.

## How to guard against the attack?

ToDo

> Note: The vulnerability is not language specific and same can be used in other languages like Java, dotnet. [Read more](https://cwe.mitre.org/data/definitions/502.html)
