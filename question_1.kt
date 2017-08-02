

fun main(args: Array<String>){
  println(find())
}

/*
Question:
Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single
line.
*/
fun find(): String{
  var result = StringBuilder()
  for (i in 2000..3201){
    if ((i % 7) == 0 && (i % 5) != 0)
      result.append("$i, ")
  }
  return result.toString().dropLast(2)//the space and comma chars
}
