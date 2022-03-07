def maxPriorities(p_list):
    p_list.sort()
    L = [0]*len(p_list)
    for i in range(len(p_list)):
        L[i] = max(L[i],p_list[i][1] - p_list[i][0])
        for j in range(i,len(p_list)):
            if(p_list[j][0] > p_list[i][1]):
                L[j] = max(L[j],L[i] + p_list[j][1] - p_list[j][0])
    return max(L)

print(maxPriorities([(1,2),(2,6),(4,6),(7,9)]))