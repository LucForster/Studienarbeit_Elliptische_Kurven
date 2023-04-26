from ellipticCurveInR import EllipticCurveInR
from ellipticCurveInFp import EllipticCurveInFp
from cyclicGroup import CyclicGroup
from DHKE import DHKE
from drawEC import DrawCurves

#ell_curve = EllipticCurveInFp(2, 2, 17)
ell_curve = EllipticCurveInFp(-3, int("0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1", 16), 6277101735386680763835789423207666416083908700390324961279)
if ell_curve.is_elliptic_curve_correct():
    print("Curve is correct!")

#gen_point = (5, 1)
gen_point = (int("0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21", 16), int("0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34", 16))
if ell_curve.is_point_on_curve(gen_point):
    print("Point is on curve!")

cyc_group = CyclicGroup(ell_curve)
#print(f"Subgroup of {gen_point} is: {cyc_group.get_sub_group_elements(gen_point)}")
#print(f"Oder of {gen_point} is: {cyc_group.get_element_order(gen_point)}")


dh_alice = DHKE(cyc_group)
dh_bob = DHKE(cyc_group)

alice_priv, alice_pub = dh_alice.gen_key_pair(gen_point)
bob_priv, bob_pub = dh_bob.gen_key_pair(gen_point)

print(f"Alice: Private Key: {alice_priv}; Public Key: {alice_pub}")
print(f"Bob: Private Key: {bob_priv}; Public Key: {bob_pub}")

alice_common_key = dh_alice.calc_common_key(bob_pub)
bob_common_key = dh_bob.calc_common_key(alice_pub)

if alice_common_key == bob_common_key:
    print(f"DHKE was successfull. Common key is: {alice_common_key}")

