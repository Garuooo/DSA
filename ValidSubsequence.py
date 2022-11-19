# Time Complexity O(N) , Space Complexity O(1)
def isValidSubsequence(array, sequence):
    sequence_index = 0
    array_index=0
    while(array_index<len(array) and sequence_index < len(sequence)):
        if array[array_index]==sequence[sequence_index]:
            array_index+=1
            sequence_index+=1
        else:
            array_index+=1
    if sequence_index==len(sequence):
        return True
    else:
        return False

# Time Complexity O(N) , Space Complexity O(1)
def isValidSubsequence(array, sequence):
    pointer=0
    for element in array:
        if element == sequence[pointer]:
            pointer+=1
        if pointer==len(sequence):
            return True
    return False
    
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10]))
