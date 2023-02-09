def square(value, n):
    temp = value
    value = value ** 2 % n
    print(str(temp) + "^2 mod " + str(n) + " = " + str(value))
    return value


def multiply(value, n, a):
    temp = value
    value = (value * a) % n
    print(str(temp) + " * " + str(a) + " mod " + str(n) + " = " + str(value))
    return value


def eukliedAlgo(n, e):
    r = 1
    while r != 0:
        r = n % e
        n = e
        e = r
    return n


def eukliedAlgoRekursiv(n, e):
    if e == 0:
        return n
    else:
        ggt = eukliedAlgoRekursiv(e, n % e)
        return ggt


def erweiterterEukliedAlgo(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = erweiterterEukliedAlgo(b % a, a)
        return gcd, y - (b // a) * x, x


def binExponantationInK(a, k, n):
    binary = bin(k)
    length = len(binary) - 2
    print(str(binary))
    print(str(length))

    if length == 1:
        value = a % n
    else:
        value = a
        i = 1
        while i < length:
            if binary[i + 2] == "0":
                print("0 =>")
                value = square(value, n)
                print("")
            else:
                print("1 =>")
                value = square(value, n)
                value = multiply(value, n, a)
                print("")
            i = i + 1
    print("Solution: " + str(value))
    return value


def eratosthenes(limit):
    primes = []
    for number in range(2, limit + 1):
        primes.append(number)
    # print(primes)

    for prime in primes:
        for number in primes[primes.index(prime) + 1:]:
            if number % prime == 0:
                primes.remove(number)

    print(primes)
    return primes


def eratosthenes2(limit):
    primes = []
    for number in range(2, limit + 1):
        primes.append(number)
    # print(primes)

    for prime in primes:
        multiple = 1
        factor = 2
        while multiple <= limit:
            multiple = prime * factor
            if multiple in primes:
                primes.remove(multiple)
            factor = factor + 1

    print(primes)
    return primes


def chinesischerRestsatz(a, modules):
    for m in modules:
        for mi in modules[modules.index(m) + 1:]:
            if eukliedAlgo(m, mi) > 1:
                return "Module sind nicht teilerfremd"

    m = 1
    for mi in modules:
        m = m * mi

    b = []
    for mi in modules:
        b.append(m / mi)


def remove_negs(num_list):
    # Remove the negative numbers from the list num_list.
    return [item for item in num_list if item >= 0]
