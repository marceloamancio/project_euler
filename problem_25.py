# project Euler problem 25
#answer: 4782
def find_fib(n):
  la, lb = 0, 1

  if n == 0:
    return la


  for i in range(n-1):
    lb, la = la + lb, lb

  return lb


if __name__ == '__main__':
  n = 4700
  while(len(str(find_fib(n)))<1000):
    n = n+1

  print(n)



