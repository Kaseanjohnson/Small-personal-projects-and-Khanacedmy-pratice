array1 = [1, 3, 5, 6]
target1 = 8

array2 = [4, 7, 2, 6]
target2 = 12

def two_sum(array, target):
    values = dict()

    for i, elem in enumerate(array):
        comp = target - elem
        if comp in values:
            return [values[comp], i]
        values[elem] = i
    return[]
list1 = two_sum(array1, target1)
print(list1)

list2 = two_sum(array2, target2)
print(list2)