#Prime

def isPrime(num):
    # define a flag variable
    flag = False

    if num==1:
        flag = True
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        return False
    else:
        return True


def factors(n):
    l = []
    for i in range(1, n + 1):
           if n % i == 0:
            l.append(i)
    return l


def prime_factors(n):
    pf = []
    ls = factors(n)
    for i in ls:
        if isPrime(i):
            pf.append(i)
    return pf


f = factors(42)
print(f)

f = prime_factors(42)
print(f)

f = factors(100)
print(f)

f = prime_factors(100)
print(f)