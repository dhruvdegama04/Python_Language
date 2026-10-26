"""2.Create a loop that goes through the following list: 
['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King'], and breaks the loop when it 
finds 'Burger King', printing 'Found Burger King, stopping search.'"""

food_list = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Burger King']

for food in food_list:
    if food == 'Burger King':
        print("Found Burger King, stopping search.")
        break

    