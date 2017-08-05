=begin
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
=end

def factorial2(number)
  acc = 1
  for i in 1..number
    acc = acc * i
  end
  acc
end

def factorial(number)
  if number == 0
    1
  else
    number * factorial(number-1)
  end
end

puts factorial2(8)
puts factorial(8)
