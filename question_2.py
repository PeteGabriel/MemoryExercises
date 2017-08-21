#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)

print(factorial(8)) #40320


def factorialIter(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res

print(factorialIter(8)) #40320
