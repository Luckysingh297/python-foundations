correct_username = "admin"
correct_password = "1234"

user_username = input("enter your username: ")
user_password = input("enter your password: ")

if user_username == correct_username and user_password == correct_password:
    print("Login successful")
else:
    print("Invalid credentials")