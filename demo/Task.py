"""1) WAPP to get the number from the user find febonaci series"""

n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

"""2) WAPP to find only number and print armstrong number between 1to 1000"""

no = int(input("entre num  : "))
copy=no
sum=0
while no>0:
    r=no%10
    no = int(no/10)
    print(no)
if sum==copy:
    print("Armstrong ",sum)
else:
    print("Not Armstrong ",sum)

"""for num2 in range(1, 1001):
    digits = [int(d) for d in str(num2)]
    power = len(digits)
    if sum(d ** power for d in digits) == num2:
        print(num2)"""

"""3) WAPp to find only number and print prime number between"""

start = int(input())
end = int(input())

for num3 in range(start, end + 1):
    if num3 > 1:
        for i in range(2, int(num3 ** 0.5) + 1):
            if num3 % i == 0:
                break
        else:
            print(num3)

"""4) WAPP to get the number from the user and find factorial"""

num4 = int(input())
fact = 1
for i in range(1, num4 + 1):
    fact *= i
print(fact)

"""5) WAPP to get the number from the user and sum of the digit like 
In python and no comments Python"""

num5 = int(input())
print(sum(int(d) for d in str(abs(num5))))