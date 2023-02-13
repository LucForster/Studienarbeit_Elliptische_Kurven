import numpy as np
from ellipticCurveInFp import EllipticCurveInFp


class DLPonEC:
    def __init__(self, curve):
        self.curve = curve

    def gen_key_pair(self, start_point):
        kPriv = np.random.randint(np.sqrt(self.curve.p), self.curve.p)

        # kPub = kPriv * start_point
        kPub = self.doubble_and_add(kPriv, start_point)

        return kPriv, kPub

    def doubble_and_add(self, kPriv, start_point):
        binary = bin(kPriv)
        binary = binary[3:]
        current_point = start_point
        for digit in binary:
            # Doubble
            current_point[0], current_point[1] = self.curve.add_points(current_point[0], current_point[1],
                                                                       current_point[0], current_point[1])
            if digit == "1":
                # Add
                current_point[0], current_point[1] = self.curve.add_points(current_point[0], current_point[1],
                                                                           start_point[0], start_point[1])

        return current_point


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
