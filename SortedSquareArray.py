# Time Complexity(O(N)) , Space Complexity(O(N))
def sortedSquaredArray(array):
    arr = []
    left = 0
    right = len(array)-1
    while(left<=right):
        if abs(array[left]) > abs(array[right]):
            arr.append(array[left]*array[left])
            left+=1
        else:
            arr.append(array[right]*array[right])
            right-=1
    return list(reversed(arr))

# Time Complexity(O(Nlog(N))) , Space Complexity(O(N))
def sortedSquaredArray(array):
    new_array = [ 0 for _ in array]
    index=0
    for element in array:
        new_array[index] = element*element
        index+=1
    return sorted(new_array)
print(sortedSquaredArray([-3,-2,-1,0,1,2,3]))