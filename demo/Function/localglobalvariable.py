def checkname():
    name="dhruv"
    print(name)
    
name="degama"
checkname()

def checkname1():

    global name
    name="dhruv"
    print(name)
    name="degama"
    print(name)

name="dd"
checkname1()