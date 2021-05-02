def isprime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False

    return True


m, n = map(int, input().split())

for i in range(m, n+1):
    if isprime(i):
        print(i)
