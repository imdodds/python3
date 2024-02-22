password1 = input("Enter a password: ")
password2 = input("Enter password again: ")

if password1 == password2:
  if len(password1) >= 8:
    print("Password is valid")
  else:
    print("Password must be at least 8 characters long")
else:
  print("Passwords do not match")