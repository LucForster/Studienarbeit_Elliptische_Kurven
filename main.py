from eccCrypto import ECCcrypto
from prim import primes

print("Hi, ich werde mal eine Studienarbeit zu Elliptischen Kurven")

crypto = ECCcrypto()
prime_numbers = primes()
#ggt = crypto.eukliedAlgo(12, 15)
#print(ggt)
crypto.eratosthenes(100000)
print(primes.checkPrime(100000))
