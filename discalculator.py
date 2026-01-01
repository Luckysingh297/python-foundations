amount = int(input("enter your amount"))
user_type = input("enter your user_type")
if amount >= 5000 and user_type == "prime":
    print("20% discount")
elif amount >= 3000 or user_type == "prime":
    print("10% discount")
else:
    print("no discount")