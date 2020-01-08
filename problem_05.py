# project Euler problem 05: Smallest multiple
# answer: 232792560

from functools import reduce

def prime_numbers(n):
  is_prime = [0,0,1] + [1, 0] * (n//2)
  last_prime = 2
  prime_found = [last_prime]

  i = last_prime + 1
  while( i < n):
    if is_prime[i] == 0:
      i = i + 1
      continue

    last_prime = i
    prime_found.append(last_prime)
    for j in range(2*last_prime, n, last_prime):
      is_prime[j] = 0

    i = last_prime + 1

  return prime_found

def find_prime_factors(pn, number):
  factors = []

  prime_i = 0
  while number > 1:
    factors.append(0)
    while number % pn[prime_i] == 0:
      number = number // pn[prime_i]
      factors[prime_i] += 1

    prime_i = prime_i + 1

  return factors


def merged_prime_factors(v):
  n = 100
  pn = prime_numbers(n)

  merged_pf = []
  for m in range(2,v+1):
    pf = find_prime_factors(pn, m)

    smallest, biggest = ( pf, merged_pf) if len(merged_pf) > len(pf) else (merged_pf, pf)
    smallest = smallest + ([0] * (len(biggest) - len(smallest)))
    assert len(smallest) == len(biggest)

    merged_pf = [max(a,b) for a,b in zip(smallest,biggest)]


  products =  [b**a for a, b in zip(merged_pf, pn[:len(merged_pf)])]
  return reduce(lambda x,y: x*y, products)

def print_current_example():
  v = 10
  merged_pf = merged_prime_factors(v)
  print(merged_pf)


if __name__ == '__main__':
  v = 20

  merged_pf = merged_prime_factors(v)
  print(merged_pf)


