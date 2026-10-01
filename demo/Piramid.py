"""
1
12
123
1234
12345

"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
print()

"""
1
21
321
4321
54321
"""

for i in range(1,6):
    for j in range(1,0,-1):
        print(j,end="")
print()

"""

5
54
543
5432
54321

"""

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="")
print()

"""
5
45
345
2345
12345

"""

for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end="")
print()

"""
*
**
***
****
*****

"""


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
print()


no=int(input("enter no : "))
for i in range(1,no+1):
        print("*"*i)

"""
1
10
101
1010
10101

1
01
101
0101
10101

1
11
121
1331
14641

a
ab
abc
abcd
abcde
"""

