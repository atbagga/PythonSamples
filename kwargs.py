def foobar(**kwargs):
    bar(kwargs)


def bar(kwargs):
    if(kwargs.get("a", None)):
        print(kwargs['a'])

    if(kwargs.get("c", None)):
        print(kwargs['c'])

    if(kwargs.get("b", None)):
        print(kwargs['b'])


foobar()