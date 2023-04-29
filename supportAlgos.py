import numpy as np


# # Beispiel: Erstelle eine elliptische Kurve y^2 = x^3 - 3x + 1
# curve = EllipticCurveInR(-3, 1)
#
# # Prüft, ob die erstellte elliptische Kurve korrekt ist
# print(curve.is_elliptic_curve_correct())
#
# # Gibt alle definierten Punkte auf der Kurve aus
# xValues, f1Values, f2Values = curve.getPoints()
# # for i in range(len(xValues)):
# #    print(f"({xValues[i]}, {f1Values[i]}, {f2Values[i]}")
#
# # Prüfe ob (0,1) auf der Kurve liegt
# print(curve.is_point_on_curve(1.6999999999999762, 0.901665126307913))
#
# # Punkte: (-1.1989999999987306, -1.6950859568180212), (0.31584338205487406, 0.28978863911584507)
# # Führe Punktaddition von (0,1) und (0,1) durch
# x, y = curve.add_points(-1.1989999999987306, -1.6950859568180212, 0.31584338205487406, 0.28978863911584507)
# print(
#     f"Punktaddition von (-1.1989999999987306, -1.6950859568180212) und (0.31584338205487406, 0.28978863911584507): ({x}, {y})")
#
# # Zeichne die Kurve
# draw = DrawCurves()
# draw.add_plot(xValues, f1Values)
# draw.add_plot(xValues, f2Values)
#
# draw.add_point_addition(-1.1989999999987306, -1.6950859568180212, 0.31584338205487406, 0.28978863911584507, x, y)
# draw.draw()

# Prüft, ob eine Zahl prim ist
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# euklidischer Algorithmus
def euklied_algo_recursiv(n, e):
    if e == 0:
        return n
    else:
        ggt = euklied_algo_recursiv(e, n % e)
        return ggt


# Gibt das multiplikative Inverse von a modulo m zurück
def inverse_mod(a, m):
    gcd, x, y = extended_euclidean_algorithm(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


# Implementierung des erweiterten euklidischen Algorithmus
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return gcd, y - (b // a) * x, x


# Implementierung des Siebs des Eratosthenes
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


# Entfernt negative Elemente aus einer Liste
def remove_negs(num_list):
    return [item for item in num_list if item >= 0]


# Gibt zu jeder Zahl das Quadrat modulo der Anzahl der Zahlen als Tupel (Quadrat, Wurzel) zurück
def get_squares_with_roots(candidate_list):
    squares_with_roots = []
    for x in candidate_list:
        square = (x ** 2) % len(candidate_list)
        squares_with_roots.append((square, x))

    return squares_with_roots
