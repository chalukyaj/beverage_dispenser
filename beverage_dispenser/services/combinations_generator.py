class CombinationsGenerator:
    def __init__(self, iterable):
        self.N = len(iterable)
        self.iterable = list(iterable)

    def generate(self):
        self.combinations = self.combinations(self.iterable)

    def combinations(self, elems):
        # print(elems)
        if not len(elems):
            return [[]]

        firstElem = elems[0]

        rest = elems[1:]

        combinationsNoFirst = self.combinations(rest)
        combinationsFirst = []

        for combination in combinationsNoFirst:
            combinationsFirst.append(combination + [firstElem])

        return combinationsNoFirst + combinationsFirst

    def getCombinations(self, R: int):
        if R > self.N:
            R = self.N
        finalCombinations = []
        for combination in self.combinations:
            if len(combination) == R:
                finalCombinations.append(combination)
        #print("Number of Combinations : ", len(finalCombinations))
        return finalCombinations
