# Time Complexity= O(NLOG(N)) , space complexity = O(1)
def nonConstructibleChange(coins):
    coins.sort()
    change=0
    for element in coins:
        if element>change+1:
            return change+1
        else:
            change=change+element
    return change+1
