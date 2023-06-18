def majority_element(v):
    n = len(v)
    cnt = 0
    el = None

    for i in range(n):
        if cnt == 0:
            cnt = 1
            el = v[i]
        elif el == v[i]:
            cnt += 1
        else:
            cnt -= 1

    cnt1 = 0
    for num in v:
        if num == el:
            cnt1 += 1

    if cnt1 > (n / 2):
        return el
    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majority_element(arr)
print("The majority element is:", ans)
