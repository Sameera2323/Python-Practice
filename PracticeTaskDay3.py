#Practice 1:

# age = int(input("What is your age ?"))
# if age < 13:
#     print("You are a child:")
# elif age <= 19:
#     print("You are a teenager:")
# elif <= 59:
#     print("You are an adult:")
# else:
#     print("You are a senior citizen:")

#Task 2: to check if the number is positive, negative or zero

# num= int(input("Enter a number:  "))

# if num > 0:
#     print("The number is positive")
# elif num < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")


#Task 3: ask for 2 numbers and print which is bigger

# num1= int(input("Enter the 1st number: "))
# num2= int(input("Enter the 2nd numner: "))

# if num1 > num2:
#     print(f"{num1} is bigger than {num2}")
# elif num1 < num2:
#     print(f"{num2} is bigger than {num1}")
# else:
#     print("Both numbers are equal")


#Task 4: Ask for a password and if it matches the stored password, print "Access granted", otherwise print "Access denied"

user_Password = input("Enter the password: ")

stored_Password = "Python123"

if user_Password == stored_Password:
    print("Access granted")
else:
    print("Access denied")