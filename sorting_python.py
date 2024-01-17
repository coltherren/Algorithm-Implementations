from unsorted_list_data import unsorted_list
import operator


# Set Operator
def compareFunc(high_or_low):
    if high_or_low == "low":
        compare = operator.lt
    elif high_or_low == "high":
        compare = operator.gt
    return compare


# Bubble Sort ()
def bubbleSort(list:list, high_or_low:str = "high"):
    '''Bubble Sort algorithm, high_or_low indicates which values bubble to the end of the sorted list'''
    length = len(list)
    compare = self.compareFunc(high_or_low)

    swapped = False
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if compare(list[j], list[j + 1]):
                swapped = True
                (list[j], list[j + 1]) = (list[j + 1], list[j])
        if not swapped:
            return
        

# Selection Sort ()
def selectionSort(list:list, high_or_low:str = "low"):
    '''Selection Sort algorithm, high_or_low indicates which values appear at the beginning of the sorted list'''
    length = len(list)
    compare = compareFunc(high_or_low)

    for i in range(length):
        index = i
        for j in range(i + 1, length):
            if compare(list[j], list[index]):
                index = j
        (list[i], list[index]) = (list[index], list[i])

bubbleSort(unsorted_list)
print(unsorted_list)