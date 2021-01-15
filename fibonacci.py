def fib(a, b, l):
  print(a)
  if l > 1:
    fib(b, a+b, l-1)

fib(1, 1, 1000)
