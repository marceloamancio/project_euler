# answer 4613732
def fib(n):
  prev_prev, prev, current = 1, 2, 3
  sum = 2

  while current < n:
    if current % 2 == 0:
      sum += current

    prev_prev = prev
    prev = current
    current = prev + prev_prev

  return sum

if __name__ == '__main__':
  n = 4000000
  answer = fib(n)
  print('answer:  ', answer)

