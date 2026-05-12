print('========== STUDENT SHOPPING CART SYSTEM ==========')

# student details
name = 'srusti'

# item list
items = ['pen', 'pencil', 'book']

# adding item
items.append('eraser')

# removing unwanted item
items.remove('pencil')

# prices
pen_price = 30
book_price = 80
eraser_price = 10

# bill calculation
total = pen_price + book_price + eraser_price

discount = 30

final_bill = total - discount

# output
print('Student Name :', name)
print('Items :', items)
print('Number of Items :', len(items))
print('Total Bill :', total)
print('Discount :', discount)
print('Final Bill :', final_bill)

print('==================================================')
