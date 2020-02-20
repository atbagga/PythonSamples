## What is Serialisation/Deserialisation?

> Serialisation is the process of converting a data object into a byte stream which can be stored, transmitted and later used to reconstruct the original object. Reconstruction of object is known as deserialisation. 

All modern applications use data serialisation so extensively since the data is passed on the network all the time, objects are cached on the servers, or persisted in the database. The bytes stream is later used to reconstruct the original object to make sense of the data.
Serialising/Deserialising trusted or known data (within the system boundary) is not a concern, but when the data is coming from untrusted sources like user input, it suddenly becomes prone to abuse.

## What is insecure deserialisation?
When a system tries to deserialise data from an untrusted source without appropriate measures it can be used to carry out attacks like denial or service (DOS), abuse application logic or even remotely execute code. This is called insecure or untrusted deserialisation.
Insecure Deserialisation is amongst the OWASP top 10 vulnerabilities list in last 3 years.

## Sample code

```python

```

## How to guard against the attack?

