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

def inverse_mod(a, m):
    # Berechnet das inverse Element von a modulo m
    # benutzt den Erweiterten Euklidischen Algorithmus
    if a < 0:
        a = a % m
    c, d, uc, vc, ud, vd = a, m, 1, 0, 0, 1
    while c != 0:
        q, c, d = divmod(d, c) + (c,)
        uc, vc, ud, vd = ud - q * uc, vd - q * vc, uc, vc
    if ud > 0:
        return ud
    else:
        return ud + m


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
