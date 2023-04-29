import numpy as np


class EllipticCurveInR:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def is_elliptic_curve_correct(self):
        # 4a^3 + 27b^2 darf nicht durch p teilbar sein bzw. nicht Null sein in F_p
        if 4 * (self.a ** 3) + 27 * (self.b ** 2) == 0:
            return False

        # Die Kurve ist korrekt
        return True

    def is_point_on_curve(self, x, y):
        # y^2 = x^3 + ax + b muss erfüllt sein
        return y ** 2 - x ** 3 - self.a * x - self.b == 0

    def add_points(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            # Punktaddition mit sich selbst
            s = (3 * x1 ** 2 + self.a) / (2 * y1)
        else:
            # Punktaddition von unterschiedlichen Punkten
            s = (y2 - y1) / (x2 - x1)
        x3 = (s ** 2 - x1 - x2)
        y3 = (s * (x1 - x3) - y1)

        return x3, y3

    def get_points(self):
        # Punkte auf x-Achse erzeugen
        # x = np.linspace(-5, 5, 100000, endpoint=True)
        # Funktion
        x = np.arange(-5, 5, 0.001)
        f = np.sqrt(x ** 3 + self.a * x + self.b)
        f1 = f
        f2 = -f
        return x, f1, f2

        # # Achseneigenschaften
        # startx, endx = -5, 50
        # starty, endy = -500, 500
        # # plt.axis([startx, endx, starty, endy])
        # # plt.axis('equal')
        # plt.style.use('seaborn')
        # plt.figure(num=0, dpi=500)
        # # Plotten
        # plt.grid(True)
        # # plt.legend()
        # plt.plot(x, f1)
        # plt.plot(x, f2)
        # plt.tight_layout()
        # plt.show()
