import numpy as np
from ellipticCurveInFp import EllipticCurveInFp


class DLPonEC:
    def __init__(self, cyclic_group):
        self.cyclic_group = cyclic_group

    def gen_key_pair(self, start_element):
        kPriv = np.random.randint(np.sqrt(self.cyclic_group.p), self.cyclic_group.p)

        # kPub = kPriv * start_point
        kPub = self.doubble_and_add(kPriv, start_element)

        return kPriv, kPub

    def doubble_and_add(self, d, start_point):
        binary = bin(d)
        binary = binary[3:]
        cur_point = start_point
        for digit in binary:
            # Doubble
            cur_point = self.cyclic_group.add(cur_point, cur_point)
            if digit == "1":
                # Add
                cur_point = self.cyclic_group.add(cur_point, start_point)

        return cur_point


curve = EllipticCurveInFp(2, 2, 17)
dlp = DLPonEC(curve)
startpoint = [5, 1]
# for i in range(10):
#     print(dlp.doubble_and_add(i, startpoint))

# print("===================")
# for i in range(10):
#     startpoint[0], startpoint[1] = curve.add_points(startpoint[0], startpoint[1], startpoint[0], startpoint[1])
#     print(startpoint)


startpoint[0], startpoint[1] = curve.add_points(startpoint[0], startpoint[1], startpoint[0], startpoint[1])
print(startpoint)
