# project Euler problem 04: Largest palindrome product
# answer 906609

def palindromo(a):
#  if -10 < a <10:
#    return True

  a_saved = a
  b = 0

  while a>0:
    b = b * 10 + a % 10
    a = a // 10

  return a_saved == b


def find_largest_palindromo_3digitmult(n):
    if n < 2:
        return None

    largest = -1
    range_max = 10**n - 1
    range_min = 10**(n-1) - 1
    for i in range(range_max, range_min, -1):
        for j in range(i, range_min, -1):
            m = i * j
            if palindromo(m):
                if m > largest:
                    largest = m
    return largest


if __name__ == '__main__':

    largest = find_largest_palindromo_3digitmult(3)
    print(largest)