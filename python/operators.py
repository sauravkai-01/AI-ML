
# arithmetics operators

a = 10
b = 20

print("sum ", a + b)
print("sub ", a - b)
print("multi ", a * b)
print("div ", a / b)  # b divides a
print("mod : ", a % b)  # b divides a
print(a**2)
print(a > b)


# logical operator only 3 i.e, not , and  , or

print(not (a > b))
print((7 > 6) and (6 > 5))
print((7 > 6) or (1 < 0))


# type casting

p = 5
k = 3.14
p = p + k
print(type(p))  # p -> float
m = 12.152
n = 10
m = (int)(m + n)
print(type(m))

var = "105"
var1 = (int)(var)
print(var1, type(var1))

var2 = bool(10)  # anything other than 0 is true(1)
print(var2, type(var2))
