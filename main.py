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

# Beispielkurve für Punktberechnung
# a = 1
# b = 3
# p = 11
# gen_point = (0, 5)


# Mittlere Beispielkurve
#a = 12
#b = 17
#p = 421
#gen_point = (200, 414)

# NIST Curve P-192
# a = -3
# b = int("0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1", 16)
# p = 6277101735386680763835789423207666416083908700390324961279
# gen_point = (int("0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012", 16),
#               int("0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811", 16))

ell_curve = EllipticCurveInFp(a, b, p)
if False:
    ell_curve_in_r = EllipticCurveInR(a, b)
    xValues, f1Values, f2Values = ell_curve_in_r.get_points()
    draw = DrawCurves()
    draw.add_plot(xValues, f1Values)
    draw.add_plot(xValues, f2Values)
    draw.draw()

if p < 1000000:
    if ell_curve.is_elliptic_curve_correct():
        print("Curve is correct!")
    else:
        print("Curve is NOT correct!")

if ell_curve.is_point_on_curve(gen_point):
    print("Point is on curve!")
else:
    print("Point ist NOT on curve!")

cyc_group = CyclicGroup(ell_curve)
print(f"All points on curve: {cyc_group.get_group_elements()}")
print(f"Group order: {cyc_group.get_group_order()}")
print(f"All Subgroups: {cyc_group.get_all_sub_groups()}")
print(f"Primitive Elements: {cyc_group.get_primitive_elements()}")

if p < 1000000:
    print(f"Subgroup of {gen_point} is: {cyc_group.get_sub_group_elements(gen_point)}")
    print(f"Order of {gen_point} is: {cyc_group.get_element_order(gen_point)}")

dh_alice = DHKE(cyc_group)
dh_bob = DHKE(cyc_group)

alice_priv, alice_pub = dh_alice.gen_key_pair(gen_point)
bob_priv, bob_pub = dh_bob.gen_key_pair(gen_point)

print(f"Alice: Private Key: {alice_priv}; Public Key: {alice_pub}")
print(f"Subgroup of {alice_pub} is: {cyc_group.get_sub_group_elements(alice_pub)}")
print(f"Bob: Private Key: {bob_priv}; Public Key: {bob_pub}")
print(f"Subgroup of {bob_pub} is: {cyc_group.get_sub_group_elements(bob_pub)}")

alice_common_key = dh_alice.calc_common_key(bob_pub)
bob_common_key = dh_bob.calc_common_key(alice_pub)

print(f"Alice common key: {alice_common_key}")
print(f"Bob common key: {bob_common_key}")

if alice_common_key == bob_common_key:
    print(f"DHKE was successfull! Common key is: {alice_common_key}")
else:
    print(f"DHKE was NOT successfull!")
