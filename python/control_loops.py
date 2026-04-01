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
