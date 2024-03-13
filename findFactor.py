import random, math

class combo:
    def combine(self, _set):
        combos = []
        if len(_set) > 1:
            for i in range(len(_set)):
                for y in _set[i]:
                    #print(_set[:i] + _set[i + 1:])
                    combs = self.combine(_set[:i] + _set[i + 1:])
                    for j in range(len(combs)):
                        combs[j].append(y)
                        combos.append(combs[j])
            return combos
        else:
            return [[element] for element in _set[0]]

    def clean(self, cmb):
        cleaned = []
        for set in cmb:
            if len(cleaned):
                for final in cleaned:
                    same = True
                    for element in set:
                        if element not in final:
                            same = False
                            break
                    if same:
                        break
                if same:
                    continue
                else:
                    cleaned.append(set)

            else:
                cleaned.append(set)
        return cleaned

def factorial(n):
    if n != 0:
        return factorial(n-1) * n
    else:
        return 1


def isPrime(num):
    for i in range(2, num):
        rem = num % i
        if rem == 0:
            return False
    return True


def allSubsets(set):
    powerSet = {}
    for i in range(1, len(set) + 1):
        maxCurLenSub = factorial(len(set))/(factorial(i)*factorial(len(set)-i))
        powerSet[i] = []
        while len(powerSet[i]) != maxCurLenSub:
            newSub = []
            for y in range(i):
                newInd = random.randint(0, len(set) - 1)
                while set[newInd] in newSub:
                    newInd = random.randint(0, len(set) - 1)
                newSub.append(set[newInd])
            same = False
            for pset in powerSet[i]:
                same = True
                if len(newSub) == len(pset):
                    for x in newSub:
                        if x not in pset:
                            same = False
                            break
                else:
                    same = False
                if same:
                    break
            if not same:
                powerSet[i].append(newSub)
    return powerSet


def writeAsSumOfPrimes(num):
    allPrimes = []
    for i in range(2, num - 1):
        if isPrime(i):
            allPrimes.append(i)
    primeSubs = allSubsets(allPrimes)
    writeSumPrime = False
    workingPrimes = None
    combi = combo()
    for length in primeSubs:
        for group in primeSubs[length]:
            mults = findWorkingMultiples(group, num)
            all_combs = combi.combine(mults)
            for i in range(len(all_combs)):
                sum = 0
                #print(group)
                for j in range(len(all_combs[i])):
                    #print(group[j], " " + str(all_combs[i][j]))

                    sum += group[j] * all_combs[i][j]

                if sum == num:
                    return [True, {str(group):all_combs[i]}]

    return [False, workingPrimes]


def findWorkingMultiples(nums, target):
    multiples = []
    for i in range(len(nums)):
        multiples.append([])
        highest = math.floor(target/nums[i])
        for j in range(highest + 1):
            multiples[i].append(j)

    return multiples

'''for i in range(1,21):
    print(i)
    print(writeAsSumOfPrimes(i))
'''
#print(writeAsSumOfPrimes(5))