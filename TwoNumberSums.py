#time complexity O(N) | space complexity O(1)
def twoNumberSum(array,target):
    for index,element in enumerate(array):
        target_number=target-element
        for second_element in array[index+1:]:
            if second_element == target_number:
                return (element,second_element)
    return []


#time complexity O(N) | space complexity O(N)
def twoNumberSum(array,target):
    hash = {}
    for element in array:
        target_number=target-element
        if hash.get(target_number) == None:
            hash[element]=True
        else:
            return [element,target_number]
    return []


#time complexity O(Nlog(N)) | space complexity O(1)
def twoNumberSum(array,target):
    array.sort()
    left=0
    right= len(array)-1
    while(left<=right):
        if array[left]+array[right]==target:
            return [array[left],array[right]]
        elif array[left]+array[right]>target:
            right-=1
        else:
            left+=1
    return []
print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],10))


