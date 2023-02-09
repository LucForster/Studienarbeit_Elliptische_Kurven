import math

# Prüft, ob eine Zahl prim ist
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class EllipticCurveInFp:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def get_points_on_curve(self):
        a = 1
        # TODO: @Aaron hier kann dein Kram für die Punktermittlung rein

    def is_elliptic_curve_correct(self):
        # p muss eine Primzahl sein
        if not is_prime(self.p):
            return False

        # p muss größer als 3 sein
        if self.p <= 3:
            return False

        # 4a^3 + 27b^2 darf nicht durch p teilbar sein bzw. nicht Null sein in F_p
        if (4 * (self.a ** 3) + 27 * (self.b ** 2)) % self.p == 0:
            return False

        # Die Kurve ist korrekt
        return True

    def is_point_on_curve(self, x, y):
        # y^2 = x^3 + ax + b muss erfüllt sein in F_p
        return (y**2 - x**3 - self.a*x - self.b) % self.p == 0

    def add_points(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            # Punktaddition mit sich selbst
            s = (3*x1**2 + self.a) * self.__inverse_mod(2*y1, self.p) % self.p
        else:
            # Punktaddition von unterschiedlichen Punkten
            s = (y2 - y1) * self.__inverse_mod(x2 - x1, self.p) % self.p
        x3 = (s**2 - x1 - x2) % self.p
        y3 = (s*(x1 - x3) - y1) % self.p
        return x3, y3

    def __inverse_mod(self, a, m):
        # Berechnet das inverse Element von a modulo m
        # benutzt den Erweiterten Euklidischen Algorithmus
        if a < 0:
            a = a % m
        c, d, uc, vc, ud, vd = a, m, 1, 0, 0, 1
        while c != 0:
            q, c, d = divmod(d, c) + (c,)
            uc, vc, ud, vd = ud - q*uc, vd - q*vc, uc, vc
        if ud > 0:
            return ud
        else:
            return ud + m

# Beispiel: Erstelle eine elliptische Kurve y^2 = x^3 + 3x + 1 modulo 7
curve = EllipticCurveInFp(3, 1, 7)

# Prüft, ob die erstellte elliptische Kurve korrekt ist
print(curve.is_elliptic_curve_correct())

# Prüfe ob (0,1) auf der Kurve liegt
assert curve.is_point_on_curve(0, 1) == True

# Führe Punktaddition von (0,1) und (0,1) durch
x, y = curve.add_points(0, 1, 0, 1)
print(f"Punktaddition von (0,1) und (0,1): ({x}, {y})")
