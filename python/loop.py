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


# odd number
k = 1
while (k <= 10):
    if (k % 2 == 0):
        k=k+1
        continue
    print(k)
    k=k+1
    
                    # for loop

print("Iterate with for loop")
name ="Saurav Kai"
for p in name:
    print(p)

print("Printing range of n : ")

for p in range(5): # from 0 to (5-1)
    print(p)


print("counting the i in word = AI")
count_i = 0
count_vowel = 0
word ="Artificial Intelligence"
for var in word:
    if (var == 'i' or var == 'I'):
        count_i = count_i + 1
for vari in word:
        if (vari == 'a' or vari == 'e' or vari == 'i' or vari == 'o' or vari == 'u'):
            count_vowel = count_vowel +1
print("Number of i : ", count_i)
print("number of vowel : ", count_vowel)


# case-1
print("range(5) : ")  # [0,5)
for i in range(5):
    print(i)

# case-2
print("range(1,6) : ")  # [1,6)
for i in range(1,6):
    print(i)

# case-3
print("range(1,20,2)")
for i in range(1, 20, 3):
    print(i)

sum = 0
print("sum of 10 natural language : ")
for i in range(11):
    sum = sum + i
print("sum : ", sum)


# using range function
