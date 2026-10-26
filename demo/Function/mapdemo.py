l1=[1,2,3,4,5]
def square(n):

    return(n*n)
l2=list(map(square,l1))
print(l2)

def cube(n):
    return(n*n*n)
l3=list(map(cube,l1))
print(l3)

l4=list(map(lambda n:n*n,l1))
print(l4)