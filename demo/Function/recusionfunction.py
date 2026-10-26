def factoriyal(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factoriyal(n-1)
print(factoriyal(5))