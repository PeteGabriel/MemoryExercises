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

Level 2

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
