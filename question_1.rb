=begin
Question:
Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single
line.
=end
def findNumbers()
  results = []
  for newNumber in 2000..3201
     results << newNumber unless (newNumber % 7) != 0 && (newNumber % 5) == 0
  end
  puts results.join(", ")
end

findNumbers()
