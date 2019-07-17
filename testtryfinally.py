"""
this is a try catch sample
"""


try:
    print('Try:')
    S = 'this is a' \
        'string'
    print(S)
    raise Exception("Custom exception")
except RuntimeError as ex:
    print('Except:')
    print(ex)
finally:
    print('Finally:')
    print(S)
