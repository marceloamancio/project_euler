# Project Euler problem 10: Summation of primes
# answer: 142913828922

def prime_numbers(n):
    is_prime = [0, 0, 1] + [1, 0] * (n // 2)
    last_prime = 2
    prime_found = [last_prime]

    i = last_prime + 1
    while (i < n):
        if is_prime[i] == 0:
            i = i + 1
            continue

        last_prime = i
        prime_found.append(last_prime)
        for j in range(2 * last_prime, n, last_prime):
            is_prime[j] = 0

        i = last_prime + 1

    return prime_found


def find_primes_below_n(n, t_max=4000000):  # n max is 2 millions
    pn = prime_numbers(t_max)
    for i, elem in enumerate(pn):
        if elem >= n:
            return pn[:i]


if __name__ == '__main__':
    total = 2000000
    b2m = find_primes_below_n(total)
    answer = sum(b2m)
    print(answer)



