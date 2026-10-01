#for loops 
#string value in a loop to performed single charaecter print one by one in new line

s="dhruv"
print(type(s))
for i in s:
    print(i,end="")

print()

#using with list though print the value via loop

lists=[1,2,"dhruv",11.11]
for i in lists:
    print(i)


#use a range data type
#print a number
print(end="| ")
for i in range(1,11):
    print(i,end=" | ")
print()

#odd number
for i in range(1,11,2):
    print(i,end="",sep="|")
print()

#even number
for i in range(2,11,2):
    print(i,end="",sep="|")
print()

#reverce number
for i in range(10,1,-1):
    print(i,end="",sep="|")
print()

#sum 

sum=0
print(type(sum))
num=int(input("enter a num="))
for i in range(1,num,2):
    print(i)
    sum+=i
    #else use or not
else:
    print("sum is...",sum)
