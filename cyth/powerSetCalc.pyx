def genPSet(_set, size, previousCalcs = []):
    subsets = []

    # Returns the only subset of the set of the same size as the set (the set itself)
    if size == len(_set):
        subsets.append(_set)
    # Returns the only subsets of size 1 on the set (each element of the set)
    elif size == 1:
        for x in _set:
            subsets.append([x])
    else:
        # Goes through each element of the provided set
        for x in _set:
            #print("Prev calcs for " + str(x) + " " + str(previousCalcs))
            # Calculates all subsets of the current set of one size less than the current
            for p in previousCalcs:
                # Adds the current element of the set to the current subset selected
                y = list(p)
                y.append(x)
                # Gets rid of all duplicate values in the subset
                # This includes all values made by adding x to the set
                _y = clean(y)
                already = False
                # Goes through the current calculation of subsets and checks if the newly generated subset is already
                # present
                for z in subsets:
                    if equal(_y, z):
                        already = True
                        break
                if len(_y) == size and not already:
                    subsets.append(_y)

    return clean(subsets)


def subsetof(self, setb):
    for y in self:
        if y not in setb:
            return False
    return True


def equal(seta, setb):
    if subsetof(seta, setb) and subsetof(setb, seta):
        return True
    else:
        return False


def clean(sets):
    '''
    Simply removes all duplicates from the input set
    :param sets: A list
    :return: A non-repeating list of elements from the input set
    '''
    clean = []
    for x in sets:
        if x not in clean:
            clean.append(x)
    return clean


def calcPSetOf(seta):
    '''
    Calculates the power set of input set.
    :param seta: a list of elements
    :return: A list of all subsets of seta
    '''

    powerSet = []
    calculatedSizes = [genPSet(seta, 1)]
    # Iterates through all sizes less than the size of the given set (except zero)
    for i in range(1, len(seta) + 1):
        if i != 1 and i != len(seta):
            sizeSet = genPSet(seta, i, calculatedSizes[i - 2])
            calculatedSizes.append(sizeSet)
        else:
            sizeSet = genPSet(seta, i)

        for x in sizeSet:
            powerSet.append(x)

    # Adds the empty set to the powerset
    powerSet.append(list())
    return powerSet

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)