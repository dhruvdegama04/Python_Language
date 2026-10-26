# to pass parameter nut not return value 
def addition(a,b):
    print("addition is",a+b)
addition(10,20)

#to pass parameter but return value

def addition1(a, b):
    return(a+b)

sum=addition1(10,20)
print("addition is",sum)

#no parameters and no return type

def addition2():
    a=10
    b=20
    print("addition no both is",a+b)

addition2()

#no parameters and but return type

def addition3():
    a=10
    b=20
    c=30
    d=a+b+c
    return d

d=addition3()
print("addition c is",d)