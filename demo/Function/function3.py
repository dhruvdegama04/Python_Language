#default value

def default(a,b,c,d=4):
    print("sum is",a+b+c+d)

default(1,2,3)

#default value

def default1(a,b,c,d): # to pass the default value in the function at lastly not in between
    print("sum s",a+b+c+d)
default1(1,2,8,10)

def default2(a,b=20,d=30): # to pass the default value in the function at lastly not in between
    print("sum s",a+b+d)
default2(a=10)

def default3(a=10,b=20,c=30): # to pass the default value in the function at lastly not in between
    print("sum s",a+b+c)
default3(a=10,c=20)