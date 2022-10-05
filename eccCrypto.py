#This class supplies mathods used for ECC Cryptograpie
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
