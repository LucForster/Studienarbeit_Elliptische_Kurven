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

    def eukliedAlgoRekursiv(self, n, e):
        if e == 0:
            return n
        else:
            ggt = self.eukliedAlgoRekursiv(e, n % e)
            return ggt

    def erweiterterEukliedAlgo(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.erweiterterEukliedAlgo(b % a, a)
            return gcd, y - (b // a) * x, x


    def EEA(self, n, e):
        nValues = []
        eValues = []
        rValues = []
        while True:
            r = n % e
            nValues.append(n)
            eValues.append(e)
            rValues.append(r)
            n = e
            e = r
            if rValues[-1] == 1:
                break
        print(r)
        print(nValues[-1])
        print(eValues[-1])
        while True:
            f1 = [1,1]
            f2 = [1,1]
            f1[1] = rValues.pop()
            f2[1] = eValues.pop()

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
        for number in range(2, limit + 1):
            primes.append(number)
        # print(primes)

        for prime in primes:
            for number in primes[primes.index(prime) + 1:]:
                if number % prime == 0:
                    primes.remove(number)

        print(primes)
        return primes

    def eratosthenes2(self, limit):
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


    def chinesischerRestsatz(self, a, modules):
        for m in modules:
            for mi in modules[modules.index(m) + 1:]:
                if self.eukliedAlgo(m, mi) > 1:
                    return "Module sind nicht teilerfremd"

        m = 1
        for mi in modules:
            m = m * mi

        b = []
        for mi in modules:
            b.append(m/mi)


