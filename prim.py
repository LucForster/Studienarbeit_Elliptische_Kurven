def eratosthenes(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


class Primes:
    'Diese Funktion gibt die Primzahlen bis zu einer eingegebenen Zahl n als Liste zurück'

    'Diese Funktion prüft, ob eine Zahl eine Primzahl ist und gibt ein True für "Ist eine Primzahl" und ein False für "Ist keine Primzahl" zurück'

    def checkPrime(self, n):
        primes = eratosthenes(n + 1)
        end = False
        if n in primes:
            return True
        return False

    #        for x in primes:
    #            if x == n:
    #                end = True
    #        return end

    def isPrime(self, n):
        for j in range(2, n):
            if n % j == 0:
                break
        else:
            return True
        return False

    def findPrimes(self, bottom, top):
        primes = []
        for value in range(bottom, top):
            if self.isPrime(value):
                primes.append(value)
        return primes
