age = int(input("enter your age"))
citizen = input("enter your citizen ?(yes/no")
has_id = input("enter your id ? (yes/no)")

if age < 18 :
    print("Age restriction")
elif citizen != "yes":
    print("Not a citizen")
elif has_id != "yes":
    print("ID missing")
else:
    print("eligible")