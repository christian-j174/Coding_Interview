def twoSum(array, target):
    result = []
    for index, value in enumerate( array ):
        for index2, value2 in enumerate( array ):
            if (value + value2) == target and (index != index2):
                return [index, index2]


# TESTS

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))