def majorityelement(A):
    n = len(A)
    cnt1 = 0
    cnt2 =0
    elt1 = -1
    elt2 = -2
    ls = []
    for i in range(n):
        if cnt1 == 0 and elt2 != A[i]:
            cnt1 = 1
            elt1 = A[i]
        elif cnt2 == 0 and elt1 != A[i]:
            cnt2 = 1
            elt2 = A[i]   
        elif A[i] == elt1:
            cnt1 +=1
        elif A[i] == elt2:
            cnt2 +=1
        else:
            cnt1 -=1
            cnt2-=1
    cnt1 = 0
    cnt2 =0
    for i in range(n):
        if elt1 == A[i]:
            cnt1 +=1
        if elt2 == A[i]:
            cnt2 +=1
    mini = int(n / 3) + 1
    if cnt1 >= mini:
        ls.append(elt1)
    if cnt2 >= mini:
        ls.append(elt2)       
    return ls        
a = [2,2]   
print(majorityelement(a))    
print(len(a),2//3)