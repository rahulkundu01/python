user_name = input("Enter you name: ")
user_age = int(input("Enter you age: "))

if user_age >= 10 and (user_name[0] =='a'or user_name[0] == 'A'):
    print("You can watch the Movie")
else:
    print("You cannot watch the Movie")