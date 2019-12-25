# answer 6857

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

def find_prime_factors(number, prime_list):
  n = len(prime_list)
  factors = [0] * n

  i = 0
  while (i < n) and (number >1):
    while number % prime_list[i] == 0 :
      factors[i] += 1
      number = number // prime_list[i]
    i = i + 1

  return number, factors


if __name__ == '__main__':
    n = 7000  # Manual test on max prime value for this problem
    prime_list = prime_numbers(n)

    number = 600851475143
    number, factors = find_prime_factors(number, prime_list)
    assert number == 1
    felems = [prime_list[i] for i, x in enumerate(factors) if x == 1]
    print(felems[-1])