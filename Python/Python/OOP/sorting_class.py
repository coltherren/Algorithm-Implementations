import operator

class List:

    def __init__(self, list):
        self.list = list
        self.length = len(self.list)

    # Set Operator
    def compareFunc(self, high_or_low):
        if high_or_low == "low":
            compare = operator.lt
        elif high_or_low == "high":
            compare = operator.gt
        return compare

    # Bubble Sort ()
    def bubbleSort(self, high_or_low:str = "high"):
        '''Bubble Sort algorithm, high_or_low indicates which values bubble to the end of the sorted list'''
        length = self.length
        compare = self.compareFunc(high_or_low)

        swapped = False
        for i in range(length - 1):
            for j in range(length - 1 - i):
                if compare(self.list[j], self.list[j + 1]):
                    swapped = True
                    (self.list[j], self.list[j + 1]) = (self.list[j + 1], self.list[j])
            if not swapped:
                return
            
    # Selection Sort ()
    def selectionSort(self, high_or_low:str = "low"):
        '''Selection Sort algorithm, high_or_low indicates which values appear at the beginning of the sorted list'''
        length = self.length
        compare = self.compareFunc(high_or_low)

        for i in range(length):
            index = i
            for j in range(i + 1, length):
                if compare(self.list[j], self.list[index]):
                    index = j
            (self.list[i], self.list[index]) = (self.list[index], self.list[i])
