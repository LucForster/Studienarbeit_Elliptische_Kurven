from ellipticCurveInFp import EllipticCurveInFp


class CyclicGroup:
    def __init__(self, elliptic_curve):
        self.elliptic_curve = elliptic_curve

    def add_elements(self, A, B):
        C = self.elliptic_curve.add(A, B)
        return C

    def scalar_dot_element(self, scalar, element):
        binary = bin(scalar)
        binary = binary[3:]

        # double and add algorithm
        current_element = element
        for digit in binary:
            # double
            current_element = self.add_elements(current_element, current_element)
            if digit == "1":
                # add
                current_element = self.add_elements(current_element, element)
        return current_element

    def get_sub_group_elements(self, primitive_element):
        current_element = primitive_element
        sub_group_elements = []
        while True:
            sub_group_elements.append(current_element)
            current_element = self.add_elements(current_element, primitive_element)
            if current_element == primitive_element:
                break

        return sub_group_elements

    def get_element_order(self, element):
        sub_group_elements = self.get_sub_group_elements(element)
        order = len(sub_group_elements)
        return order

    def get_group_order(self):
        group_elements = self.elliptic_curve.get_all_points_on_curve()
        group_order = len(group_elements)
        return group_order

    def get_group_elements(self):
        return self.elliptic_curve.get_all_points_on_curve()

    def get_all_sub_groups(self):
        elements = self.get_group_elements()
        checked_elements = []
        sub_groups = []
        for element in elements:
            if element not in checked_elements:
                sub_group = self.get_sub_group_elements(element)
                checked_elements.extend(sub_group)
                sub_groups.append(sub_group)

        return sub_groups

    def get_primitive_elements(self):
        elements = self.get_group_elements()
        group_order = self.get_group_order()
        primitive_elements = []
        for element in elements:
            if self.get_element_order(element) == group_order:
                primitive_elements.append(element)

        return primitive_elements


# scalar = 19
# bin_scalar = bin(scalar)[2:]
# print(bin_scalar)
# bin_scalar = bin_scalar
# print(bin_scalar)
