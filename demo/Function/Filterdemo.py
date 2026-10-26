l1=[22,44,77,88,99,33]
def checkeven(n):
    if n%2==0:
        return(n)
l2=list(filter(checkeven,l1))
print("l2 is",l2)

l3=list(filter(lambda n:n%2==0,l1))
print("l3 is",l3)