# project Euler problem 07: 10001st prime
# answer 104743


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


def get_list_ll(m = 10001):
  n = 1000

  while True:
    ll = prime_numbers(n)
    if len(ll) < m :
      n = n * 10
    else:
      return ll


if __name__ == '__main__':
    ll = get_list_ll()
    print(ll[10000])
