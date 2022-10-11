'Diese Funktion gibt die Primzahlen bis zu einer eingegebenen Zahl n als Liste zurück'
def eratosthenes(n):
    primes = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

'Diese Funktion prüft, ob eine Zahl eine Primzahl ist und gibt ein True für "Ist eine Primzahl" und ein False für "Ist keine Primzahl" zurück'
def checkPrime(n):
    primes = eratosthenes(n+1)
    end = False
    for x in primes:
        if x == n:
            end = True
    return end

print(checkPrime(99988))