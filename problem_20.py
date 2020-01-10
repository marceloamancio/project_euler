# project Euler problem 20: Factorial digit sum
# answer: 648

def fact(n):
  number = 1
  for i in range(2,n+1):
    number *= i
  return number

if __name__ == '__main__':
  n = 100
  f = fact(n)
  answer = sum([int (x) for x in str(f)])
  print(answer)