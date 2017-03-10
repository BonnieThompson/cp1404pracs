"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

Sales = float(input("Enter sales: $"))
while Sales <0:
    Sales = float(input("Enter sales: $"))

if Sales <1000:
    amount = Sales +(Sales*0.1-Sales)
else:
    amount = Sales + (Sales * 0.15 - Sales)

print(amount)
