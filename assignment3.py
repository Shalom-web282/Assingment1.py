# # Question 1(Salary Calculator)

salary = float(input("What's your salary? "))
bonus = float(input("What's your Bonus? "))
tax_rate = float(input("What's your tax rate? "))

gross = salary + bonus
tax = tax_rate * gross
net = gross - tax
print(f"Gross:${gross:,.2f}")
print(f"Tax:${tax:,.2f}")
print(f"Net:${net:,.2f}")

# # Question 2(Login systems-3 attempts)

username = "Shalom"
Password = "abc123"
for i in range(3):
    u_name = input("Enter your username: ")
    pwrd = input("Enter your password: ")

    if u_name == username and pwrd == Password:
        print("Welcome back")
        break
    else:
        print("Incorrect credentials")
else:
    print("Accout blocked")

# Question 3(Student Grade AnaLyzer)

scores = []
for i in range(1,5):
    score = float(input(f"Enter your score {i}: "))
    scores.append(score)
average = sum(scores)/4
if 70<= average <= 100:
    grade = "A"
elif 60<= average <= 69:
    grade = "B"
elif 50<= average <= 59:
    grade = "C"
else:
    grade = "F"
print("highest score:", max(scores))
print("minimum score:", min(scores))
print(f"Average: {average:.1f}")
print("Grade:", grade)

#Question 4(ATM Withrawal Simulation)

Act_bal = float(5000)
amount = float(input("Enter withdrawal amt: "))
bal = Act_bal - amount
if amount > Act_bal:
    print("Insufficient funds")
    
elif amount <= 0:
    print("Invalid amount")
else:
    print(f"New balance: ${bal:,.2f}")

# Question 5(Membership Login)

members = ("favour", "Blessing", "Joy")
password = "abc123" 
name = input("Enter your name? ")
pawd = input("Enter your password? ")
if name in members and pawd == password:
    print("Access granted")
elif name in members and pawd != password:
    print("Incorrect Password")
else:
    print("Not registered")

#Question 6(Phone Network Checker)

contact = str(input("Enter your number? "))
code = contact[0:3]

MTN = "070"
MTN = "080"
Airtel = "081"
Glo = "090"

if code == "070":
    print("Welcome to MTN network")
elif code == "080":
    print("Welcome to MTN network")
elif code == "081":
    print("Welcome to Airtel network")
elif code == "090":
    print("Welcome to Glo network")
else:
    print("Unknown network")

#Question 7(Two-Number Comparison)

first_num = float(input("Enter a number: "))
second_num = float(input("Enter a second number: "))

if first_num > second_num:
    print("First_num is larger")
elif second_num > first_num:
    print("second_num is larger")
else:
    print("Both numbers are equal")
third = first_num + second_num
condition = third % 2
if condition == 0:
    print("Sum of numbers is even")
else:
    print("sum of numbers is odd")

#Question 8(Shopping Discount Program)

price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))
total = price * quantity

if total >= 20000:
    discount = 0.1 * total
else:
    discount = 0

net_profit = total - discount
print("Total:", total)
print("Discount:", discount)
print("Net_Profit:", net_profit)

# Question 9(Bus Fare System)

age = int(input("Enter your age? "))
qualification = input("Are you a student?(yes/no): ").lower()

if qualification == "yes":
    fare = "Half price"
elif age < 10:
    fare = "Free"
elif 10<= age <= 17:
    fare = "Half price"
elif 18<= age:
    fare = "Full price"

print("Bus fare:", fare)

# Question 10(Electricity Bill Calculator)

units = int(input("Enter number of units used: "))

if 0 <= units <= 100:
    rate = 25
elif 101 <= units <= 200:
    rate = 35
else: 
    rate = 45

bill = units * rate
print(f"Total bill: #{bill}")
print("rate per unit:", rate)



