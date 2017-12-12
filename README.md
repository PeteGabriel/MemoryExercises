#----------------------------------------#

Question 1

Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

```python
def find():
    results = []
    for i in range(2000, 3201):
        if ((i % 7) == 0) and ((i % 5) != 0):
            results.append(i)

    print(str(results).strip('[]'))
```

#----------------------------------------#

Question 2

Level 1

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be: 40320

```ruby
def factorial(number)
  acc = 1
  for i in 1..number
    acc = acc * i
  end
  acc
end
```

#----------------------------------------#

Question 3

Level 1

With a given integral number n, write a program to generate a dictionary that contains (i, i\*i) such that is an integral number between 1 and n (both included). Then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

```ruby
def question_3(n)
  dict = {}
  (1..n).each{ |i| dict[i] = i*i }
  dict
end

puts question_3 8
```
