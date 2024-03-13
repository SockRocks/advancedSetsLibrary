from findFactor import allSubsets

class Set:
    def __init__(self, elements, universe=[]):
        clean = []
        for element in elements:
            if element not in clean:
                clean.append(element)

        self.elements = clean
        self.universe = universe

    def powerSet(self):
        pSet = []
        for x in allSubsets(self.elements).values():
            for y in x:
                pSet.append(Set(y))
        pSet.append(Set([]))
        return Set(pSet)

    @classmethod
    def union(cls, set1, set2):
        union = []
        cls.addToSetNoDup(set1.elements, union)
        cls.addToSetNoDup(set2.elements, union)
        return Set(union)

    @staticmethod
    def intersect(set1, set2):
        inter = []

        for el in set1.elements:
            if el in set2.elements and el not in inter:
                inter.append(el)
        return Set(inter)

    @staticmethod
    def cartesianProd(set1, set2):
        prod = []
        for el in set1.elements:
            for y in set2.elements:
                newElement = (el,y)
                if newElement not in prod:
                    prod.append(newElement)
        return Set(prod)

    @classmethod
    def setMinus(cls, set1, set2):
        minus = []
        for element in set1.elements:
            if element not in set2.elements:
                minus.append(element)
        return Set(minus)

    def complement(self):
        return Set.setMinus(self.elements, self.universe)

    def display(self):
        for el in self.elements:
            if type(el) == Set:
                print(el.elements)
            else:
                print(el)
    @staticmethod
    def addToSetNoDup(set, empty):
        for el in set:
            if el not in empty:
                empty.append(el)

    @staticmethod
    def setEq(set1, set2):
        for x in set1.elements:
            isIn = False
            if x in set2.elements:
                isIn = True
            if not isIn:
                return False
        return True

    def toSet(self):
        fin = set(self.elements)
        return fin

    def __len__(self):
        return len(self.elements)


    def __str__(self):
        return str(list(self.elements))

    def __mul__(self, other):
        return Set.cartesianProd(self, other)

    def __sub__(self, other):
        return Set.setMinus(self, other)

    def __list__(self):
        return self.elements