
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def save_primes_to_file(filename, start, end):
    with open(filename, 'w') as file:
        for num in range(start, end + 1):
            if is_prime(num):
                file.write(str(num) + '\n')


filename = 'results.txt'
save_primes_to_file(filename, 1, 250)
