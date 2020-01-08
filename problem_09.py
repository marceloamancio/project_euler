# Project Euler problem 09: Special Pythagorean triplet
# answer 31875000

def find_pythagorean_triplet():
  for a in range(1,1000):
    for b in range(a+1,1000):
      c = 1000 - a - b
      if c < 0 or c > 1000:
        continue

      if a**2 + b**2 == c**2:
        return a,b,c

if __name__ == '__main__':
  a,b,c = find_pythagorean_triplet()
  assert a < b < c
  assert a**2 + b**2 == c**2
  assert a+b+c == 1000

  print(a*b*c)