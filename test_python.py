def stringToDict(inputList):
    if not inputList:
        return {}
    result = {}
    for inputSet in inputList:
        parts=inputSet.split('=', 1)
        key=parts[0]
        value=parts[1]
        result[key]=value
    print(result)
    return result


print(stringToDict(['Abc=def', 'def=']))