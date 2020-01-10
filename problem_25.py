# project Euler problem 25
# answer: 4782

def find_fib(maxs):
  la, lb = 0, 1
  counter = 1

  while len(str(lb)) < maxs:
    lb, la = la + lb, lb
    counter += 1

  return counter

if __name__ == '__main__':
  answer = find_fib(1000)

  print(answer)



