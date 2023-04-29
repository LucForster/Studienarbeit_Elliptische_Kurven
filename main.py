from ellipticCurveInR import EllipticCurveInR
from ellipticCurveInFp import EllipticCurveInFp
from cyclicGroup import CyclicGroup
from DHKE import DHKE
from drawEC import DrawCurves

# Kleine Beispielkurve
a = 2
b = 2
p = 17
gen_point = (5, 1)

# Weitere kleine Beispielkurve
# a = -3
# b = 3
# p = 13
# gen_point = (4, 4)


# Mittelgroße Beispielkurve
# a = 12
# b = 17
# p = 421
# gen_point = (200, 414)

# NIST Curve P-192
# Bitte Beachten: Bei Verwendung dieser Kurve haben wegen der hohen Anzahl an Punkten einige Funktionen z.B. jene
# zur Bestimmung aller Punkte eine extrem hohe Laufzeit, weshalb sie nicht genutzt werden können
# a = -3
# b = int("0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1", 16)
# p = 6277101735386680763835789423207666416083908700390324961279
# gen_point = (int("0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012", 16),
#               int("0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811", 16))

# Elliptische Kurve initialisieren
ell_curve = EllipticCurveInFp(a, b, p)

# Zeichnen der Kurve kann durch Eintragen von True aktiviert werden
if False:
    ell_curve_in_r = EllipticCurveInR(a, b)
    xValues, f1Values, f2Values = ell_curve_in_r.get_points()
    draw = DrawCurves()
    draw.add_plot(xValues, f1Values)
    draw.add_plot(xValues, f2Values)
    draw.draw()

# Zu große Laufzeit bei großen p
if p < 1000000:
    # Prüft, ob die elliptische Kurve korrekt definiert ist
    if ell_curve.is_elliptic_curve_correct():
        print("Curve is correct!")
    else:
        print("Curve is NOT correct!")

# Prüft, ob der Generatorpunkt auf der Kurve liegt
if ell_curve.is_point_on_curve(gen_point):
    print("Generator-Point is on curve!")
else:
    print("Generator-Point ist NOT on curve!")

# Zyklische Gruppe auf Basis der elliptischen Kurve initialisieren
cyc_group = CyclicGroup(ell_curve)

# Zu große Laufzeit bei großen p
if p < 1000000:
    print(f"All elements of group: {cyc_group.get_group_elements()}")
    print(f"Group order: {cyc_group.get_group_order()}")
    print(f"All Subgroups: {cyc_group.get_all_sub_groups()}")
    print(f"Primitive elements: {cyc_group.get_primitive_elements()}")
    print(f"Subgroup of {gen_point} is: {cyc_group.get_sub_group_elements(gen_point)}")
    print(f"Order of {gen_point} is: {cyc_group.get_element_order(gen_point)}")

# Initialisieren zweier DHKE Objekte mit der zyklischen Gruppe zum Durchführen eines Schlüsselaustauschs
dh_alice = DHKE(cyc_group)
dh_bob = DHKE(cyc_group)

# Erzeugung zweier Schlüsselpaare
alice_priv, alice_pub = dh_alice.gen_key_pair(gen_point)
bob_priv, bob_pub = dh_bob.gen_key_pair(gen_point)

# Ausgabe der generierten Schlüssel und der Untergruppen der öffentlichen Schlüssel
print(f"Alice: Private Key: {alice_priv}; Public Key: {alice_pub}")
# Zu große Laufzeit bei großen p
if p < 1000000:
    print(f"Subgroup of {alice_pub} is: {cyc_group.get_sub_group_elements(alice_pub)}")
print(f"Bob: Private Key: {bob_priv}; Public Key: {bob_pub}")
# Zu große Laufzeit bei großen p
if p < 1000000:
    print(f"Subgroup of {bob_pub} is: {cyc_group.get_sub_group_elements(bob_pub)}")

# Berechnung des gemeinsamen geheimen Schlüssels
alice_common_key = dh_alice.calc_common_key(bob_pub)
bob_common_key = dh_bob.calc_common_key(alice_pub)

# Ausgabe der berechneten Schlüssel
print(f"Alice common key: {alice_common_key}")
print(f"Bob common key: {bob_common_key}")

# Prüfung ob der DHKE erfolgreich war, d.h. ob beide Parteien den gleichen Schlüssel berechnet haben
if alice_common_key == bob_common_key:
    print(f"DHKE was successfully! Common key is: {alice_common_key}")
else:
    print(f"DHKE was NOT successfully!")
