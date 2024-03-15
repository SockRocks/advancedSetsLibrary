from findFactor import allSubsets
import newLib

class Set:
    def __init__(self, elements, universe=[], multiSet=False):
        self.elements = elements
        self.current = 0
        
        if not multiSet:
            self.elements = self.duplicateRemoval()

    def __len__(self):
        return len(self.duplicateRemoval())

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
        return str(list(self))
    
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

    def duplicateRemoval(self):
        clean = []
        for element in self.elements:
            if element not in clean:
                clean.append(element)
        return clean

    def powerSet(self):
        pSet = []
        for x in allSubsets(self.elements).values():
            for y in x:
                pSet.append(Set(y))
        pSet.append(Set([]))
        return Set(pSet)

