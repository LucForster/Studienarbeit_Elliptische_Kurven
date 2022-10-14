from eccCrypto import ECCcrypto
from prim import Primes

print("Hi, ich werde mal eine Studienarbeit zu Elliptischen Kurven")

crypto = ECCcrypto()
prime_numbers = Primes()
#ggt = crypto.eukliedAlgo(12, 15)
#print(ggt)
#crypto.eratosthenes(100000)
#print(Primes.checkPrime(prime_numbers, 100000))

values = [10000000000013, 94273, 94291, 94307, 94309, 94321, 94327, 94331, 94343, 94349, 94351, 94379, 94397, 94334]
for value in values:
    print(Primes.isPrime(prime_numbers, value))

print(prime_numbers.findPrimes(1099000, 1099100))
