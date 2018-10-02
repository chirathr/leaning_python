def get_primes(start):
    while True:
        if is_prime(start):
            yield start
        start += 1

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
        
    i = 5
    while (i * i < number):
        if number % i == 0 or number % (i / 2) == 0:
            return False
        i += 6
    return True


for i in range(100):
    if is_prime(i):
        print(i)
