from eccCrypto import ECCcrypto

print("Hi, ich werde mal eine Studienarbeit zu Elliptischen Kurven")

crypto = ECCcrypto()
ggt = crypto.eukliedAlgo(12, 15)
print(ggt)
crypto.eratosthenes(100000)
