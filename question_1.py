#---
#Question 1
#Level 1

#Question:
#Write a program which will find all such numbers which are divisible by 7
#but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single
#line.

BOTTOM_LIMIT = 2000
TOP_LIMIT = 3200

def find():
    #One common way to build large strings from pieces is to grow a
    #list of strings and join it when you are done.
    #This is a frequently-used Python idiom.
    results = []
    for i in range(BOTTOM_LIMIT, TOP_LIMIT + 1):
        if ((i % 7) == 0) and ((i % 5) != 0):
            results.append(i)

    print(str(results).strip('[]'))


find()
