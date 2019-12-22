
def sum_multiples_3and5(n):

  s = 0
  for i in range(3, n):
    if (i % 3 == 0) or ( i % 5 == 0):
      s += i

  return s

n = 1000

if __name__ == '__main__':
  print(sum_multiples_3and5(n))