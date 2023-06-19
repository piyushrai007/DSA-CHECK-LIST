# using hash-table or python dictionary --> time complexity is O(n)
#-->space complexity O(n)
def majorityelement(A):
    ls =[]
    n = len(A)//3 
    a ={}
    for i in range(len(A)):
        if A[i] in a:
            a[A[i]] += 1
        else:
            a[A[i]] = 1
        if a[A[i]] == (n+1):
            ls.append(A[i])
    return ls        
a = [1,1,1,3,3,2,2,2]   
print(majorityelement(a)) 