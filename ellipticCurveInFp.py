import math
import supportAlgos


class EllipticCurveInFp:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def get_all_points_on_curve(self):
        x_values = []
        points = []
        if not self.is_elliptic_curve_correct():
            return False
        # Berechnen der Quadrate und zugehörige Wurzeln in F_p
        squares_with_roots = supportAlgos.get_squares_with_roots(range(self.p))
        # Liste mit Quadraten erstellen
        squares = []
        for tupel in squares_with_roots:
            if tupel[0] not in squares:
                squares.append(tupel[0])
        # Prüfe für jedes x in F_p, ob es eingesetzt ein Quadrat ergibt
        for x in range(self.p):
            if (x ** 3 + self.a * x + self.b) % self.p in squares:
                x_values.append(x)
        # Ermitteln der Punkte auf der Kruve
        points = []
        for x in x_values:
            y_quad = (x ** 3 + self.a * x + self.b) % self.p
            for tupel in squares_with_roots:
                if y_quad == tupel[0]:
                    points.append((x, tupel[1]))
        # Neutrales Element hinzufügen
        points.append(("N", "N"))
        return points

    def is_elliptic_curve_correct(self):
        # p muss eine Primzahl sein
        if not supportAlgos.is_prime(self.p):
            return False

        # p muss größer als 3 sein
        if self.p <= 3:
            return False

        # 4a^3 + 27b^2 darf nicht durch p teilbar sein bzw. nicht Null sein in F_p
        if (4 * (self.a ** 3) + 27 * (self.b ** 2)) % self.p == 0:
            return False

        # Die Kurve ist korrekt
        return True

    def is_point_on_curve(self, P):
        x, y = P
        if x == "N":
            return True
        # y^2 = x^3 + ax + b muss erfüllt sein in F_p
        return (y ** 2 - x ** 3 - self.a * x - self.b) % self.p == 0

    def add(self, P, Q):

        if not self.is_point_on_curve(P):
            return None
        if not self.is_point_on_curve(Q):
            return None

        x1, y1 = P
        x2, y2 = Q
        # Addition des neutralen Elements mit sich selbst ergibt das neutrale Element
        if x1 == "N" and x2 == "N":
            R = ("N", "N")
            return R
        # Addition eines Punktes und des neutralen Elements ergibt den Punkt
        elif x1 == "N":
            R = (x2, y2)
            return R
        elif x2 == "N":
            R = (x1, y1)
            return R
        # Addition inverser Punkte ergibt neutrales Element
        elif x1 == x2 and y1 != y2:
            R = ("N", "N")
            return R

        # Addition nach bekannten Formeln
        if x1 == x2 and y1 == y2:
            # Punkt ist Nullstelle --> Tangente ist parallel zur y-Achse --> ergibt neutrales Element
            if y1 == 0:
                R = ("N", "N")
                return R

            # Punktaddition mit sich selbst
            s = (3 * x1 ** 2 + self.a) * supportAlgos.inverse_mod(2 * y1, self.p) % self.p
        else:
            # Punktaddition von unterschiedlichen Punkten
            s = (y2 - y1) * supportAlgos.inverse_mod((x2 - x1) % self.p, self.p) % self.p
        x3 = (s ** 2 - x1 - x2) % self.p
        y3 = (s * (x1 - x3) - y1) % self.p
        R = (x3, y3)
        return R
