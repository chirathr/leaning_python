def get_primes(start):
    # generator that returns prime number from start
    while True:
        if is_prime(start):
            yield start
        start += 1

def is_prime(number):
    # Check if number if prime
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while (i * i) <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


def solve_number_10():
    #Project Euler #10: sum of prime number till 2000000
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

solve_number_10()
