# # #name = "Hello Shalom"
# # #print(name)
# # #DEMOPprint('Hello World')

# name = "Shalom"
# age= 19
# print(f"My name is {name}.\nI am {age} years old.")
# 
# name = ['Shalom', 'Chimdike', 'Favour', 'Grace']
# w, x, y, z = name 
# print(w, x, y, z)

# print("My name is Shalom.\nI'm a software developer.\nI'm 23 years old.")
# x = "God "
# y = "is "
# z = "Good "
# w = "All  the time"
# print(x, y, z, w)
# x = "awesome"

# def myfunc():
#     print("Python is " + x)

# myfunc()  

# x = "God"

# def myGod():
#     print("My " + x + " Is good")

# myGod()  

# x = "awesome"

# def myfunc():
#     x = "fantastic"
#     print("python is " + x)
# myfunc()  

# # print("Python is " + x)
# print("He is called 'Johnny'")
# print('He is called "johnny"')

# a = "Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."
# print(a)

# Strings are arrays
# a = "Shalom"
# print(a[5])

# # Looping through a string
# for x in "banana":
#     print(x)
# # String length
# # The len() function returns the length of a string:
# a = "Hello world"
# print(len(a))
# a = ['Mango', 'Orange', 'Guava']
# print(len(a))
# print(len(a[2]))

#Check string

# txt = "The best things in life are free!"
# print("free" in txt)
# msg = "Shalom Shoes your go-to for quality handmade shoes"
# print("Shoes" in msg)

# print("Shoes" in txt)
# print("baxie" in msg)

# String Creation
# s = 'Hello World'
# h = "Hello World"
# l = """Hello World"""
# print(s, h, l)

# # Assigning a variable
# a = "Python is fun to learn"
# print(a)


# # # Multiline String
# c = "Python is Powerful.\nIt is easy to learn.\nIt is loved by developers"
# print(c)

# # //String as Arrays

# b = "PYHON"
# print(b[0])
# print(b[2])
# print(b[4])

# # Looping Through a String
# for x in "Python":
#     print(x)
# for m in "Shalom":
#     print(m)    

# # String Length and Checking
# fruit = "banana"
# print(len(fruit))

# word = "Learning Python is cool."
# if "Python" in word:
#     print("Yes, 'Python' is in word.")

# if "Java" not in word:
#     print("'Java' is not found in the sentence.")


# name = "Ada"
# age = 18
# school = "Bright Future Academy"
# print(f"My name is {name}, I am {age} years old, and i attend {school}")

# country = "Nigeria"
# capital = "Abuja"
# print(f"The capital of {country} is {capital}.")

# first_name = "John "
# middle_name = "Paul "
# last_name = "Okoro"
# print(first_name, middle_name, last_name)

# food = "Rice"
# drink = "Juice"
# print(f"I love eating {food} with {drink}.")


# # Counting how many times "n" appears
# message = "Coding is fun"
# count = 0
# for char in message:
#     if char == "n":
#         count += 1
# print(count)    

# poem = """Python makes coding simple, Python makes me solve problems fast, Python is the language i enjoy learning."""
# print(poem.upper())
# shoes = "Shalom Shoes expertly crafts ladies footwears for elegance and comfort"

# count = 0
# for char in shoes:
#     if char == "n":
#         count += 1
# print(count)

# name = " Hello World"
# print(name[6:])
# print(name.upper())
# print(name.lower())
# print(name.strip())
# print(name.replace("H", "J"))
# print(name.split(","))

# # String CONcatenation

# name = "Shalom "
# age = '28 '
# career = "Software Developer "
# nationality = "Nigeria."
# bio = name + age + career + nationality
# print(bio)

# price = 30000
# print(f"I need {price: .2f} Dollars")
# print(f"I need {price * 20} Dollars")

# Escape paragraphs

# txt = "They are the s0-called \"Vikings\" from the north."
# b = "They are the s0-called \'Vikings\' from the north."
# c = "They are the s0-called \\Vikings\\ from the north."
# d = "They are the s0-called \nfrom the north."
# e = "They are the s0-called \rVikings from the north."
# f = "They are the s0-called \tVikings\t from the north."
# g = "They are the s0-called \bVikings \bfrom the north."
# h = "They are the s0-called \fVikings\f from the north."
# i = "\150\145\154\154\157"

# variables = (txt, b, c, d, e, f, g, h, i)
# for x in variables:
#     print(x) 
# print(i)

# x = "God help me"
# print(type(x))

# fruits = ["Apple" "Guava" "Mango" "Banana"]
# for x in fruits:
#     print(x)

    # Python Lists
# unordered and no duplicates
# myset = {"Banana", "Orange", "Guava" "Banana"}
# print(myset)

# myset = {"Banana", "Guava", "Apple" "Banana", 'Cashew',  False, 0, 2}
# print(myset)

set1 = {0, True, "Red", "White"}
set2 = {"intercept", "White", False, 1}

# set3 = set2.intersection(set1)
# set4 = set1.union(set2)
# set1.intersection_update(set2)
# set5 = set2.difference_update(set1)
# print(set3)
# print(set4)
# print(set1)
# print(set5)

# fruits = ("Orange", "Mango", "Cashew")
# even_num = (2,3,4,5,6,)
# multiple_dt = ("str", 10, 0.1, ["Toyota", "Honda"])
# print(fruits[0])
# print(even_num[2:5])
# for x in fruits:
#     print(x)
# print(len(fruits)) 

# Creating  a tuple, print the second value to the last value, convert it to a list, change the value of the second value, conert it back to a tuple then print.

foods = ("Rice", "Beans", "Yam", "Plantain", "Potatoe")
print(type(foods))
print(foods[2:])

food_list = list(foods)
food_list[1] = "Spaghetti"
food_list.append
foods = tuple(food_list)

print(foods)

# Dictionary
student = {
    "name": "Shalom"
    "age": 20,

}
"""(
Create a dictionary
Print all keys

"""
students = {
    "pleasant":(85, 70),
    "Shalom":(20, 70),
    "Ada":(30, 63)
}
for student, score in student.items()
    for i in score:
        average_score += i
print(average_score )

# Study all data types
"""
(Sets)
lists
tuples
dictionary
booleans
"""






