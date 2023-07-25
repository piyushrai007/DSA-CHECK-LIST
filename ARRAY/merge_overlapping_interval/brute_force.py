from typing import *

def mergeOverlappingIntervals(arr : List[List[int]]) -> List[List[int]]:
    # Write your code here.
    pass
    arr.sort()
    lst = []
    for i in range(len(arr)):
        start = arr[i][0]
        end = arr[i][1]
        if len(lst)!=0  and end <= lst[-1][-1]:
            continue
        for j in range(i+1,len(arr)):
            if arr[j][0] <= end:
                end = max(end,arr[j][1])
            else:
                break    
        lst.append([start,end])
    return lst
a = [[1,2],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]   
b = mergeOverlappingIntervals(a) 
print(b)   






