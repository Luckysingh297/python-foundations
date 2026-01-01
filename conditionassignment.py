username = "admin" 
password = "1234"

user_name = input("enter username:").strip()
user_password = input("enter password:").strip()

if user_name == username and user_password == password:
     print("login successful")
else :
    print ("Invalid credentials")