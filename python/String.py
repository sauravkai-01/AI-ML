word = "saurav kai"
print(word)

# length of string

print("length of ", word, " : ", len(word))

# contamination
word1 = "hello"
word2 = "world"
print(word1+word2)

# indexing value

word3 = "Bengaluru"
print(word3[0])
print(word3[1])

print("Indexing : ")
for i in range(len(word3)):
    print(word3[i],end="") # end="" prevent from new line



# slicing
print("\nslicing : ")
str = "python is easy"
str1 = str[0: 3]
print(str1, str[4: 11])
print(str[2:])
print(str[-11: -3])
