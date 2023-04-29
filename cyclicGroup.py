class CyclicGroup:
    def __init__(self, elliptic_curve):
        self.elliptic_curve = elliptic_curve

    # Addiert zwei Gruppenelemente
    def add_elements(self, A, B):
        C = self.elliptic_curve.add(A, B)
        return C

    # Multipliziert einen Skalar mit einem Gruppenelement unter Verwendung des Double-And-Add-Algorithmus
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

    # Gibt zu einem gegebenen Element die durch dieses erzeugte Untergruppe zurück
    def get_sub_group_elements(self, primitive_element):
        current_element = primitive_element
        sub_group_elements = []
        while True:
            sub_group_elements.append(current_element)
            current_element = self.add_elements(current_element, primitive_element)
            if current_element == primitive_element:
                break

        return sub_group_elements

    # Gibt die Ordnung eines gegebenen Elements zurück
    def get_element_order(self, element):
        sub_group_elements = self.get_sub_group_elements(element)
        order = len(sub_group_elements)
        return order

    # Gibt die Ordnung der Gruppe zurück
    def get_group_order(self):
        group_elements = self.elliptic_curve.get_all_points_on_curve()
        group_order = len(group_elements)
        return group_order

    # Gibt alle Elemente der Gruppe zurück
    def get_group_elements(self):
        return self.elliptic_curve.get_all_points_on_curve()

    # Gibt alle Untergruppen der zyklischen Gruppe zurück
    def get_all_sub_groups(self):
        sub_groups = []
        sub_group_generators = []
        divisors = []
        order = self.get_group_order()
        primitive_elements = self.get_primitive_elements()
        # Finden von echten Teilern der Gruppenordnung
        for number in range(1, int(order / 2 + 1)):
            if order % number == 0:
                divisors.append(number)
        # Berechnen der Untergruppen-Generatoren
        for div in divisors:
            sub_group_generators.append(self.scalar_dot_element(int((order / div)), primitive_elements[0]))
        # Berechnen der Untergruppen
        for gen in sub_group_generators:
            sub_groups.append(self.get_sub_group_elements(gen))
        return sub_groups

    # Gibt alle primitiven Elemente der zyklischen Gruppe zurück
    def get_primitive_elements(self):
        elements = self.get_group_elements()
        group_order = self.get_group_order()
        primitive_elements = []
        for element in elements:
            if self.get_element_order(element) == group_order:
                primitive_elements.append(element)

        return primitive_elements
