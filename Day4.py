# Step 1: While loop

# count=1
# while count <=5:
#     print(f"Count is : {count} " )
#     count +=1


#Step 2: For loop

# for i in range(5):
#     print(f"i is : {i}")

# Step 3: For loop with strings or list

# word= "Python"
# for letter in word:
#     print(letter)


# fruits= ["Apple", "Banana", "Kiwi"]
# for fruit in fruits:
#     print(f"I like {fruit}")


# # Step 4: For loop with break
# for num in range(1, 10):
#     if num==5:
#         print("Using break command")
#         break
#     print(num)


#Step 5: For loop with continue

for num in range(1, 6):
    if num==4:
        print("Trying to use continue command")
        continue
    print(num)