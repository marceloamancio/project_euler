# Project Euler problem 14 - Longest Collatz sequence
# answer 837799

UPPERL = 15000000
vec = [-1]*UPPERL

def col(n):

  if n<=1:
    return 1

  if n < UPPERL and vec[n] != -1:
      return vec[n]

  next_n = None
  if n%2 == 0:
    next_n = n//2
  else:
    next_n = 3*n + 1

  ans = 1 + col(next_n)
  if n < UPPERL:
    vec[n] = ans

  return ans


if __name__ == '__main__':
  col_list = [col(x) for x in range(1,1000000)]
  maxn = max(col_list)
  answer = col_list.index(maxn) + 1

  print(answer)

