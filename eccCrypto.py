# This class supplies mathods used for ECC Cryptograpie
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


class ECCcrypto:
    def __init__(self):
        self.testattribut = None

    def eukliedAlgo(self, n, e):
        r = 1
        while r != 0:
            r = n % e
            n = e
            e = r
        return n

    def binExponantationInK(self, a, k, n):
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

    def eratosthenes(self, limit):
        primes = []
        for number in range(2, limit+1):
            primes.append(number)
#        print(primes)

        for prime in primes:
            for number in primes[prime.__index__():]:
                if number % prime == 0:
                    primes.remove(number)

        print(primes)
        return primes

