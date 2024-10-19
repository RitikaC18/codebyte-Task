def second_largest(arr):
    #checking atleast Two numbers Are Present
    if len(arr) < 2:
        return None  

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
            
    return second if second != float('-inf') else None


array = [14, 11, 23, 42, 39, 16]
print(second_largest(array))

#output:39