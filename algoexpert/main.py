def isValidSubsequence(array, sequence):
    acc = 0
    for element in array:
        if len(sequence) > 1:
            if element == sequence[acc]:
                acc += 1
        else:
            if element == sequence[acc]:
                return True
            return False
    
    if acc == len(sequence):
        return True
    return False
