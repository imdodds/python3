subtotal = input("Enter the total before tip: ")
tip_percentage = input("Enter the tip percentage: ")
people = input("Enter the number of people: ")

total = float(subtotal) * (1 + float(tip_percentage) / 100)
per_person = total / int(people)

print("Each person should pay: ", per_person)