from copy import copy


class PermutationsGenerator:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.length = len(self.iterable)
        self.results = []

    def generate(self):
        self.recurse(0, self.length - 1)
        return self.results

    def swap(self, pos1, pos2):
        self.iterable[pos1], self.iterable[pos2] = (
            self.iterable[pos2],
            self.iterable[pos1]
        )

    def recurse(self, start, end, depth=0):
        if start == end:
            self.results.append(copy(self.iterable))
        else:
            for ind in range(start, end+1):
                self.swap(start, ind)
                # print(start, end, self.get_beverages_order())
                self.recurse(start + 1, end, depth + 1)
                self.swap(ind, start)
