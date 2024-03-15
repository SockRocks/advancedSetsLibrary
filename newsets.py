class Set:
    def __init__(self, *elements, universe=[], multiSet=False):
        self.current = 0
        self.multiSet = multiSet
        if len(elements) == 1 and type(elements[0]) == list:
            elements = elements[0]

        if not self.multiSet:
            elements = self.duplicateRemoval(elements)
        self.universe = universe
        self.elements = self.toSet(elements)
    
    def __len__(self):
        return len(self.duplicateRemoval(self.elements))

    def __iter__(self):
        return self

    def __setitem__(self, index, newitem):
        self.elements[index] = newitem

    def __getitem__(self, index):
        return self.elements[index]

    def __next__(self):
        if self.current < len(self):
            c = self.current
            self.current+= 1
            return self.elements[c]
        else:
            self.current = 0
            raise StopIteration

    def __str__(self):
        return str(self.__list__())
    
    def __list__(self):
        return_list = []
        for i in range(len(self)):
            return_list.append(0)
        
        for i in range(len(self.elements)):
            mutable = False
            
            try:
                test_dict = dict()
                test_dict[self.elements[i]] = 1
            except TypeError:
                mutable = True
            if isinstance(self.elements[i], Set):
                mutable = True
            
            if mutable:
                return_list[i] = list(self.elements[i])
            else:
                return_list[i] = self.elements[i]
        return return_list

    def __set__(self):
        return set(self.__list__())

    def toSet(self, elements):
        return_list = []
        for i in range(len(elements)):
            return_list.append(0)
        range(len(elements))
        for i in range(len(elements)):
            mutable = False
            
            try:
                testDict = dict()
                testDict[elements[i]] = 1
            except TypeError:
                mutable =True
                
            if isinstance(elements[i], Set):
                mutable = False
            
            if mutable:
                return_list[i] = Set(elements[i], universe=self.universe, multiSet=self.multiSet)
            else:
                return_list[i] = elements[i]
        return return_list
        
    def duplicateRemoval(self, elements):
        clean = []
        for element in elements:
            if element not in clean:
                clean.append(element)
        return clean

    '''def powerSet(self):
        pSet = []
        for x in allSubsets(self.elements).values():
            for y in x:
                pSet.append(Set(y))
        pSet.append(Set([]))
        return Set(pSet)'''
        
    @staticmethod
    def genPSet(_set, size):
        subsets = []

        if size == len(_set):
            subsets.append(_set)
        elif size == 1:
            for x in _set:
                subsets.append([x])
        else:
            for x in _set:
                for y in genPSet(_set, size-1):
                    y.append(x)
                    _y = clean(y)
                    already = False
                    for z in subsets:
                        if equal(_y, z):
                            already = True
                            break
                    if len(_y) == size and not already:
                        subsets.append(_y)

        return clean(subsets)
    
    def subsetof(seta, setb):
        for y in seta:
            if y not in setb:
                return False
        return True
    def equal(seta, setb):
        if subsetof(seta, setb) and subsetof(setb, seta):
            return True
        else:
            return False

    def clean(sets):
        clean = []
        for x in sets:
            if x not in clean:
                clean.append(x)
        return clean

    def calcPSetOf(seta):
        powerSet = []
        for i in range(1, len(seta)+1):
            for x in genPSet(seta, i):
                powerSet.append(x)
        powerSet.append(list())
        return powerSet


    def powerSet(set):
        pSet = []
        for x in allSubsets(set).values():
                for y in x:
                    pSet.append(y)
        pSet.append(list())
        return pSet



a = Set([1,2,3],2,3, 3, multiSet=True)
print(a)