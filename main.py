from ellipticCurveInR import EllipticCurveInR
from drawEC import DrawCurves

# Beispiel: Erstelle eine elliptische Kurve y^2 = x^3 - 3x + 1
curve = EllipticCurveInR(-3, 1)

# Prüft, ob die erstellte elliptische Kurve korrekt ist
print(curve.is_elliptic_curve_correct())

# Gibt alle definierten Punkte auf der Kurve aus
xValues, f1Values, f2Values = curve.getPoints()
# for i in range(len(xValues)):
#    print(f"({xValues[i]}, {f1Values[i]}, {f2Values[i]}")

# Prüfe ob (0,1) auf der Kurve liegt
print(curve.is_point_on_curve(1.6999999999999762, 0.901665126307913))

# Punkte: (-1.1989999999987306, -1.6950859568180212), (0.31584338205487406, 0.28978863911584507)
# Führe Punktaddition von (0,1) und (0,1) durch
x, y = curve.add_points(-1.1989999999987306, -1.6950859568180212, 0.31584338205487406, 0.28978863911584507)
print(
    f"Punktaddition von (-1.1989999999987306, -1.6950859568180212) und (0.31584338205487406, 0.28978863911584507): ({x}, {y})")

# Zeichne die Kurve
draw = DrawCurves()
draw.add_plot(xValues, f1Values)
draw.add_plot(xValues, f2Values)

draw.add_point_addition(-1.1989999999987306, -1.6950859568180212, 0.31584338205487406, 0.28978863911584507, x, y)
draw.draw()
