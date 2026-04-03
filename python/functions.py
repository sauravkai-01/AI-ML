                        # Non-parametric function

def hello():
    print("hello world")
    print("this is saurav kai")
    print("i am the best")

hello()

                      # parametric function


def sum(a, b):
    print("sum : ", (a + b ))
sum(10, 20)

print("having return type : ")
def sum(a, b):
    return (a + b)
print("sum : ", sum(10, 20))


print("average of  three number : ")
def sum(a, b, c):
    s = (a + b + c)/3
    return s


print("Average of 10 20 30 : ", sum(10, 20, 30))
def sum(a, b=2):
    return (a+b)
print("sum : ", sum(5))

                        # lamda function

sum = lambda a, b, c:a+b+c
print("lambda sum : ", sum(10,20,52.2))

print("factorial of num : ")
def fact(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    return factorial

print(fact(7))
