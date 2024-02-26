subtotal = input("Enter the subtotal: ")
hst = 0.13
tax = float(subtotal) * hst
total = float(subtotal) + tax

print("The tax is: ", tax)
print("The total is: ", total)