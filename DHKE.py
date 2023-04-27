import numpy as np
import math
from decimal import Decimal
import random


class DHKE:
    def __init__(self, cyclic_group):
        self.cyclic_group = cyclic_group
        self.k_priv = None
        self.k_pub = None

    def gen_key_pair(self, start_element):
        group_order = self.cyclic_group.get_element_order(start_element)

        # k_priv = random.randrange(int(np.sqrt(10000000000000000000)), 10000000000000000000)
        k_priv = np.random.randint(np.sqrt(group_order), group_order)

        # kPub = kPriv * start_point
        k_pub = self.cyclic_group.scalar_dot_element(k_priv, start_element)

        self.k_priv = k_priv
        self.k_pub = k_pub

        return k_priv, k_pub

    def calc_common_key(self, k_pub):
        common_key = self.cyclic_group.scalar_dot_element(self.k_priv, k_pub)
        return common_key
