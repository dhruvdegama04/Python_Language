"""1.Define a function called get_discounted_price that takes price and discount_percent
 as arguments and returns the final price after applying the discount. 
 Test it with a price of 500 and a discount of 10%.
"""

def get_discounted_price(price, discount_percent):
    discount_amount = (price * discount_percent) / 100
    return price - discount_amount

final_price = get_discounted_price(500, 10)
print(final_price)