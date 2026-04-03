                        # while loop 
i = 1
while (i <= 10):
    print("value of i : ", i)
    i = i+1

# multiple of 11

n = 1
while (n <= 10):
    if (n == 5):
        n = n+1
        continue 
    print(11, " x ", n, " = ", n*11)
    n = n+1
    if (n == 9):
        break
