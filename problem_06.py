# project Euler problem 06: Sum square difference
# answer 25164150

def sum_of_the_squares(n):
  return ( n * (n+1) * (2*n+1) )// 6

def square_of_the_sum(n):
  return ( ( n * (n+1) )  // 2) ** 2

if __name__ == '__main__':
  n = 100
  ss = sum_of_the_squares(n)
  ss2 = square_of_the_sum(n)
  result = ss2-ss
  print(ss2-ss)