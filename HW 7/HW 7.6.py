import time

def simple_prime_search(limit):
    start_time_1 = time.time()
    simple_numbers_1 = []
    for number in range (limit + 1):
        is_prime = True
        if number < 2:
            continue
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            simple_numbers_1.append(number)
    print(simple_numbers_1)
    stop_time_1 = time.time()
    print("Time Taken:", stop_time_1 - start_time_1)


def sieve_eratosthenes(limit):
    start_time_2 = time.time()
    simple_numbers_2 = [True] * (limit + 1)
    simple_numbers_2[0] = simple_numbers_2[1] = False
    for i in range(limit + 1):
        if simple_numbers_2[i]:
            for j in range(i * i, limit + 1, i):
                simple_numbers_2[j] = False
    prime_numbers = [i for i, prime in enumerate(simple_numbers_2) if prime]
    print(prime_numbers)
    stop_time_2 = time.time()
    print("Time Taken:", stop_time_2 - start_time_2)


sieve_eratosthenes(100)
simple_prime_search(100)


