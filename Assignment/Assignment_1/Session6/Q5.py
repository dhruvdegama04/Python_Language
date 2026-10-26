"""5.Create a program that uses a while loop to print a pyramid star pattern with 4 rows,
 so the output looks like BookMyShow's seat rows:
*
***
*****
*******
<br><br><em><strong>Hint:</strong> Use two nested while loops: one for spaces, 
one for stars.</em>"""

rows = 4
i = 1

while i <= rows:
    spaces = rows - i
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    
    stars = 2 * i - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
        
    print()
    i += 1