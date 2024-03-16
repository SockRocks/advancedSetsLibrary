from powerSetCalc import calcPSetOf

class Set:
    count = 0
    def __init__(self, *elements, universe=[]):
        # Iteration variable for tracking iterations
        self.current = 0

        # If the user mistakenly enters a single list to contain all elements then that list is converted into an
        # elements list
        if len(elements) == 1 and (type(elements[0]) == list or type(elements[0]) == tuple):
            elements = elements[0]

        self.elements = elements
        elements = self.duplicateRemoval()
        # universe of discourse
        self.universe = universe
        # Converts each iterable element in the set into a set object
        self.elements = tuple(self.toSet(elements))
        self.isProduct = False
    
    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        # This is strictly used for the beginning of iteration
        return self

    '''def __setitem__(self, index, newitem):
        self.elements[index] = newitem
    '''

    def __getitem__(self, index):
        # Used for brackets element accessing
        return self.elements[index]

    def __next__(self):
        # Accesses the next element during iteration
        if self.current < len(self):
            c = self.current
            self.current += 1
            return self.elements[c]
        else:
            self.current = 0
            raise StopIteration

    def __str__(self):
        return str(self.__list__()).replace("[", '{').replace(']','}')

    def __list__(self):
        '''
        Converts the current instance of the set object into a standard list (along with each of its set elements)
        :return: A list of the elements the set
        '''

        return_list = []
        for i in range(len(self.elements)):
            return_list.append(0)
        
        for i in range(len(self.elements)):
            mutable = False

            # Checks if the current element is mutable
            try:
                test_dict = dict()
                test_dict[self.elements[i]] = 1
            except TypeError:
                mutable = True
            if isinstance(self.elements[i], Set) or type(self.elements[i]) == tuple:
                mutable = True
            
            if mutable:
                # If the current element is mutable, then it's converted to a list
                # notice that even set objects will call the current method to convert to a list until the primitive
                # types are reached
                return_list[i] = list(self.elements[i])
            else:
                # If an element is not mutable than it can be added to the return list as is
                return_list[i] = self.elements[i]
        return return_list

    def __set__(self):
        return set(self.__list__())

    def __eq__(self, other):
        return self.equal(other)

    def __abs__(self):
        return len(self)

    def __add__(self, other):
        return self.union(other)

    def __sub__(self, other):
        return self.setMinus(other)

    def __and__(self, other):
        return self.intersection(other)

    def __mul__(self, other):
        return self.cartesianProduct(self,other)

    def union(self, setb):
        Set.count = 0
        result = []

        for x in self:
            if x not in result:
                result.append(x)
        for x in setb:
            if x not in result:
                result.append(x)

        return Set(result)

    def setMinus(self, setb):
        Set.count = 0
        result = []

        for x in self:
            if x not in setb:
                result.append(x)
        return Set(result)

    def complement(self):
        return self.setMinus(self.universe)

    def intersection(self, setb):
        Set.count = 0
        result = []

        for x in self:
            if x in setb:
                result.append(x)

        return Set(result)

    def toSet(self, elements):
        '''
        A helper function used to convert a list of elements to a set; however the constructor should be called for this
        purpose not this method
        :param elements: A list of elements
        :return: A list of elements where all mutable elements have been converted to set objects
        '''

        return_list = []

        # Extends the return list to be the length of the number of elements submitted
        for i in range(len(elements)):
            return_list.append(0)

        for i in range(len(elements)):
            mutable = False

            # Checks to see if the current element is mutable
            try:
                testDict = dict()
                testDict[elements[i]] = 1
            except TypeError:
                mutable = True

            # The set class is not considered mutable
            if isinstance(elements[i], Set):
                mutable = False
            
            if mutable:
                # Converts the current element to a set object
                return_list[i] = Set(elements[i], universe=self.universe)
            else:
                # If the current object is a base type, then it does not need to be converted and is kept as is
                return_list[i] = elements[i]
        return return_list
        
    def duplicateRemoval(self):
        '''
        Removes duplicate elements from the given set object (this is not intended to be called from outside the class
        :return: A list of non-repeating elements
        '''
        clean = []
        Set.count = 0
        for element in self.elements:
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

    def powerSet(self):
        '''
        Calculates the power set of a set
        :return: A power set set object
        '''
        Set.count = 0

        _self = self.__list__()
        powerSet = calcPSetOf(_self)
        return Set(powerSet)


    def subsetof(self, setb):
        '''
        Checks if the current set is a subset of the input set
        :param setb: comparison set
        :return: Is this set is a subset of setb
        '''
        Set.count = 0

        for y in self:
            if y not in setb:
                return False
        return True

    def equal(self, setb):
        '''
        This set is equal to set b
        :param setb:
        :return:
        '''
        Set.count = 0

        if self.subsetof(setb) and setb.subsetof(self):
            return True
        else:
            return False

    def setDisplayMode(self):
        '''
        Displays each element of the current set by hitting enter each time. This is a good way to display a very long
        set especially when copying
        :return:
        '''
        Set.count = 0

        for x in self:
            print(x, end="\n")
            input()

    def cartesianProduct(self, *setb):
        result = []
        if len(setb) == 1:
            for x in self:
                for y in setb:
                    result.append((x,y))
        else:
            for i in range(len(self)):
                for y in self.cartesianProduct(setb[i:]):
                    _y = list(y)
                    _y.append(self[i])
                    result.append(tuple(_y))
        return result

    def aCartesianProduct(self, seta, *setb):
        result = []

        if len(setb) == 1:
            for x in seta:
                print(setb)
                for y in setb[0]:
                    #print("D: " + str(y))
                    result.append((x,y))
            #print(result)
        else:
            for i in range(len(seta)):
                for y in self.aCartesianProduct(setb[i], setb[i+1:]):
                    #print(y)
                    _y = list(y)
                    _y.append(seta[i])
                    result.append(tuple(_y))

        return result
