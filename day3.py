print(2 == "2")
print("hari" != "Hari")


print(True and True)
print(2 == 2 and 1 != 3)
a = 5
b = 10


print(a >= b and b == a)


a = True
print("not operator...", not (a))


"""

if (True and True):
    print("this is hello")
    ....
    ....
    .,,

"""
if 6 >= 4:
    print("this is inside from true condition")

else:
    print("this is else condition")


if 6 >= 4:
    print("this is inside from true condition")
    a = 10

else:
    print("else")

num = 4
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


if 2 == 2:
    print("this is if condition")
elif 1 == 2:
    print("this is elif")

elif 1 != 4:
    print("this is also elif")

else:
    print("else")


# marks = int(input("Enter your percentage: "))
marks = 1
if marks >= 80 and marks <= 100:
    print("DIs")
elif marks <= 79 and marks >= 60:
    print("1st ")
else:
    print("Failed or wrong input")


# nested if condition

# marks = int(input("Enter your percentage: "))
marks = 1
if marks >= 80 and marks <= 100:
    if 2 == 2:
        print("this is true")
    elif marks == 80:
        print("Perfect dis")
    elif marks == 100:
        print("Highest percentage")


elif marks <= 79 and marks >= 60:
    print("1st ")
else:
    print("Failed or wrong input")


n = -110
if n > 0:
    if n % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
elif n == 0:
    print("number is neither positive nor negative")
else:
    print("number is negtive")


account_balance = 10000
# withdrawn_amount = int(input("Enter the amount to be withdraw : "))
withdrawn_amount = 800

if account_balance > withdrawn_amount:
    if withdrawn_amount % 100 == 0:
        print("amount can be withdrawn")
        x = account_balance - withdrawn_amount

        print("withdrawn_amount amount is", withdrawn_amount)
        print("remaining balance is", x)
    else:
        print("try amount which is multiple of 100")

else:
    print("withdrawl amount is bigger than account amount")


gender = "M"

if gender == "M":
    print("male")
else:
    print("Female")

data = "Male" if gender == "M" else "Female"
print(data)
