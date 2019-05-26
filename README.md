# python
Python Training Examples

ex 01:
Program to guess the number: (nested if statement)
print("Number gussing game:")
winning_number = 27
user_input = int(input("Guess a number between 1 and 100: " ))
if user_input == winning_number:
    print("You Win!!!!!!!")
else:
    if user_input < winning_number:
        print("Number is too low")
    else:
        print("Number is too high")
        

ex 02:
Program to check if the entered number is even or odd:
print("This is the program to check that the enter number is even or odd:")
n = int(input("Enter the value of n: "))
if n%2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")
