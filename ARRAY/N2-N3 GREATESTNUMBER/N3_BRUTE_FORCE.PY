def majorityelement(A):
    ls =[]
    n = len(A)//3
    print(n)
    for i in range(len(A)):
        # print(len(ls),ls[0])
        if len(ls)==0 or ls[0] != A[i]:
            count =0
            for j in range(len(A)):
                if A[i] ==A[j]:
                    count+=1
            if count > n:
                ls.append(A[i])   
        if len(ls) ==2:
            break     
    return ls  
a = [1,1,1,3,3,2,2,2]   
print(majorityelement(a))                  