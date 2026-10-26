#palindrom

no=int(input("enter number"))
copy=no
sum=0
while no > 0:
    t=no%10
    sum=(sum*10) + t
    no=int(no/10)
    print(no)
if sum == copy:
    print("palindrom number",sum)
else:
    print("not palindrom number",sum)


#armstrong 

no1=int(input("enter number"))
copy1=no1
sum1=0
while no1 > 0:
    t1=no1%10
    sum1=sum1+(r*r*r)
    no1=int(no1/10)
    print(no1)
if sum1 == copy1:
    print("armstrong number",sum1)
else:
    print("not armstrong number",sum1)

#piramiddemo3

for i in range(1,6):
    print(" "*(5-i),"*"*i)

for i in range(1,6):
    print(" "*(5-i)," *"*i)

for i in range(1,6):
    print("*"*i)

for i in range(5,0,-1):
    print("*"*i)

#piramid demo 2

for i in range(1,6):
    for j in range(1,i+1):
        print(j%2,end="")
    print()

k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end="")
        k=k+1
    print()
    
for i in range(97,102):
    for j in range(97,i+1):
        print(chr(j),end="")
    print()