/*
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
*/

fun main(args: Array<String>) {
  println(factorial(8))
}


fun factorial(num: Int): Int{
  if (num == 0) return 1 else return num * factorial(num-1)
}
