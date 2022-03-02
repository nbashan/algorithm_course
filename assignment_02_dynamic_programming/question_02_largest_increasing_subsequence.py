def largest_increasing_subsequence(array):
    ret = 0
    length_array = [1] * len(array)
    index_stack = []

    for i in range(1, len(array)):
        temp_stack = []
        for j in range(i):
            if array[j] <= array[i] and length_array[j] + 1 > length_array[i]:
                temp_stack.append(array[j])
                length_array[i] = length_array[j] + 1
        temp_stack.append(array[i])
        if length_array[i] > ret:
            index_stack = temp_stack
            ret = length_array[i]
    return ret,index_stack


print(largest_increasing_subsequence([-1, 3, 4, 5, 2, 2, 5, 2]))
