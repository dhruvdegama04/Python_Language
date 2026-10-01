#1 condition - If

no1=10
if no1>=10 :
    print("this number is gretar then 10.",no1)

#2 condition - If Else
#to find odd or even with out using % (module)

no2=101
if no2%2 == 0 :
    print("This number is even..",no2)
else :
    print("This number is odd..",no2)

#3 condition - Nested If

no3=-0
if no3 >= 0 :
    if no3 == 0 :
        print("This Number IS zero",no3)
    else :
        print("this number is positive",no3)
else :
    print("this number is nagative",no3)

#4 condition - If Else..If

no4=10
no5=20
no6=30

if no4>no5 and  no4>no6 :
    print("a is max",no4)
elif no5>no4 and no5>no6 :
    print("b is max",no5)
else :
    print("c is max",no6)

#multiple comment (''',"""")

'''no4=100
no5=100
no6=100

if no4>=no5 and  no4>no6 :
    print("a is max",no4)
elif no5>no4 and no5>=no6 :
    print("b is max",no5)
else :
    print("c is max",no6)

'''

"""no4=10
no5=20
no6=30

if no4>=no5 and  no4>=no6 :
    print("a is max",no4)
elif no5>=no4 and no5>=no6 :
    print("b is max",no5)
else :
    print("c is max",no6)

"""