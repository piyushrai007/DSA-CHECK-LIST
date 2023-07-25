from typing import *

def mergeOverlappingIntervals(arr : List[List[int]]) -> List[List[int]]:
    # Write your code here.
    pass
    arr.sort()
    lst = []
    for i in range(len(arr)):
        if len(lst) == 0 or arr[i][0] > lst[-1][-1]:
            lst.append(arr[i])
        if arr[i][0] <= lst[-1][-1] and arr[i][1]>=lst[-1][-1] :
            lst[-1][-1]= arr[i][1]
        
    return lst
a = [[1,2],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]   
b = mergeOverlappingIntervals(a) 
print(b)   

