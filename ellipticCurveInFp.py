import math
import supportAlgos


class EllipticCurveInFp:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def get_all_points_on_curve(self):
        x_squares = []
        points = []

        if self.is_elliptic_curve_correct(self) != True:
            return False

        # Speichern von berechneten Quadraten in square_candidates
        square_candidates = self.get_squares(range(self.p))

        # Finde x-Werte, welche Quadrate sind
        for x in range(square_candidates):
            temp = (x ** 3 - self.a * x - self.b) % self.p
            isPresent = temp in set(square_candidates)
            if isPresent == True:
                x_squares.append((x))
            elif isPresent == False:
                break

        # Berechne die Punkte
        for x in x_squares:
            # Berechne das Quadrat der aktuellen Zahl
            y_squared = (x ** 3 + self.a * x + self.b) % self.p
            root_1, root_2 = self.get_roots(y_squared, self.p)
            point_1 = (x, root_1)
            point_2 = (x, root_2)
            points.append(point_1)
            points.append(point_2)

        return points

    def get_squares(candidate_list):
        squares = []

        # Berechne Quadrate und speichere sie in squares
        for x in candidate_list:
            square = (x**2) % len(candidate_list)
            isPresent = square in set(squares)
            if isPresent == True:
                break
            elif isPresent == False:
                squares.append((square))
        return squares.sort()

    def check_square(x, p):
        for y in range(p):
            if (y ** 2) % (p) == x:
                return True
        return False

    def get_roots(x, p):
        roots = []
        for y in range(p):
            if (y ** 2) % p == x:
                roots.append(y)
                if len(roots) == 2:
                    break
        return roots[0], roots[1]

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
        # y^2 = x^3 + ax + b muss erfüllt sein in F_p
        return (y ** 2 - x ** 3 - self.a * x - self.b) % self.p == 0

    def add(self, P, Q):
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
