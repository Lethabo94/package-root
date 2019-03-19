def sum_array(array):
    if type(array) == int:
        return array

    sum = 0
    for e in array:
        if type(e) == array:
           sum = sum+sum_array(e)
        else:
            sum = sum+e
    return sum

    def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


        def factorial(n):
   num = 1
   while n >= 1:
       num = num * n
       n = n - 1
   return num


   def reverse(word):
  name = ""
  for i in word:
    name = i + name
  return name
