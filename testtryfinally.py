"""
this is a try catch sample
"""

def get_s():
    raise Exception("My error")
    return "this is s"

try:
    print('Try:')
    S = get_s()
    print(S)
    # raise Exception("Custom exception")
except RuntimeError as ex:
    print('Except:')
    print(ex)
finally:
    print('Finally:')
    print(S)

print('Outside Try catch:')
print(S)