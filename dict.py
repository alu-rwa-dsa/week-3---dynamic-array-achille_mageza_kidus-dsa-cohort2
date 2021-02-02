Dictionary={"car":"Nisaan","version":"2009","matriculation":"12348"}
def add(keys,result):
    Dictionary[keys]=result
    print(Dictionary)

def remove(keys):
    Dictionary.pop(keys)
    print(Dictionary)


def modification(keys,newresult):
    Dictionary[keys]=newresult
    print(Dictionary)


def find(Keys):
    Keys=Dictionary.keys()
    print(Keys)


find("car")