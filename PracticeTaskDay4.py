# #Task 1: Print numbers from 1 to 10 using while
# count=1
# while count<=10:
#     print(f"Number is : {count}")
#     count +=1

# #Task 2: Print even numbers from 2 to 20 using for

# for num in range(2, 21, 2):
#     if num %2==0:
#         print(f"Number is even: {num}")


# #Task3: Loop through the word "Sameera" and print each letter

# word= "Sameera"
# for letter in word:
# 	print(letter)


# #Task 4:Ask user to enter numbers until they type 0, then print the sum

# sum= 0
# while True:
#     num= int(input("Enter a number (0 to stops): "))
#     if num ==0:
#         print(f"You entered: {num}")
#         break
#     sum += num
# print(f"Final total sum is: {sum}")


#Task 5: Print a simple pattern
# *
# * *
# * * *
# * * * * 

for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print() # for Next line
