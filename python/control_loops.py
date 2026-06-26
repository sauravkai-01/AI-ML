age = int(input("Enter age : "))

if age <= 0:
    print("Invalid age : ")
elif age >= 18 and age <= 25:
    print("you are mature")
    print("you can marry")
elif age > 25:
    print("you need to build a home")
    print("working professional")
    print("earn money")
else:
    print("you are minor")
    print("padhai kar")



username = input("Enter username : ")
password = input("Enter password : ")

if (username == "admin" and password == "admin@123"):
    print("welcome")
    print("login succeed !")
elif (username != "admin"):
    print("invalid username")    
elif (username == "admin" and password != "admin@123"):
    print("invalid password")
else:
    print("login failed !!")

# even odd
number = int(input("Enter number : "))
if (number % 2 == 0):
    print(number, " : Even")
else:
    print(number, " : Odd")
