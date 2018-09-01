"""

Assingment number 1

The cover price of a book is $25, but bookstores get a 10% discount. Shipping costs $2
for the first five copies and 2.75 cents for all rest of copies. Write a Python program to
show what is the total wholesale cost for 40 copies display the result.

SOUMIL SHAH
Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Engineering


"""
# Declare all the values mentioned in problem

total_book= 40
cost_price = 25
discount = 10/100
shipping_5 = 2
shipping_rest_35 = 2.75

# cost of book withouth Discount
Book_cost_no_discount = 40 * 25

# Cost of book with Discount
book_cost_discount = Book_cost_no_discount - (discount * Book_cost_no_discount)

# Calculate shipping cost of 5 books
shipping_5_book= 2 * 5

# Calculate shipping cost of rest of books
shipping_35_book = shipping_rest_35 * 35

# calculate maths for all book
wholesale_cost= book_cost_discount + shipping_5_book + shipping_35_book

# print Result
print("Whole Sale Cost of 40 Books is  $ {} ".format(wholesale_cost))


