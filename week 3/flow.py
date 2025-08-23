def calculate_discount(price, discount_percent):
    # price and discount_percent are now assumed to be numbers
    if discount_percent >= 20:
        discount_price = price * (discount_percent / 100)
        final_price = price - discount_price
        return final_price
    else:
        return price

# Q2 Getting user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Now pass numbers to the function
final_price = calculate_discount(original_price, discount_percentage)

# Compare numbers, not strings
if discount_percentage >= 20:
    print(f"Discount applied: {discount_percentage}%") 
    print(f"Final price: {final_price}")
else:
    print(f"No discount was applied. Original price: {original_price}")
