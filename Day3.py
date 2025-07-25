#Step1: basic else if statement

# age = int(input("Enter your age: "))

# if age >=18:
#     print("You are an adult")

# else:
#     print("Yoy are a minor")

#Step2: using elif statement

# score= int(input("Enter your Master's score: "))

# if score >= 90:
#     print("You have got A grade in Master's")

# elif score >=75:
#     print("You have got B grade in Master's")

# elif score >=60:
#     print("You have got C grade in Master's")

# elif score >=50:
#     print("You have got D grade in Master's")

# else:
#     print("You have failed in Master's")


#Step3: Logical operators

age= int(input("Enter you age: "))

has_licence=True

if age >=18 and has_licence:
    print("You can drive a car")

else:
    print("You cannot drive a car, you are either underage or do not have a licence")   