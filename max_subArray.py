#brute force 
def max_sub_array(arr,n):
    max_difference = 0
    for i in arr:
        for j in range (i+1,n):
            b=arr[j]-arr[i]
            # print(b)
            max_difference = max(max_difference,b)
    return max_difference
#divide and conquer method 
def min_element(a, l, u):
    min_elt = 9999999999999999999999999999999999
    for i in range(l, u+1):
        min_elt = min(min_elt, a[i])
    return min_elt


def max_element(a, l, u):
    max_elt = 0
    for i in range(l, u+1):
        max_elt = max(max_elt, a[i])
    return max_elt


def _max_sub_array(arr, l, u):
    # base conditions
    if u == l:
        return 0
    elif u == l + 1:
        return max(arr[u] - arr[l], 0)
    else:
        m = (l + u) // 2
        # recursion
        m1 = _max_sub_array(arr, l, m)
        m2 = _max_sub_array(arr, m + 1, u)
        # straddling condition
        y1 = max_element(arr, m + 1, u)
        y2 = min_element(arr, l, m)
        print(y1, y2)

        return max(m1, m2, (y1 - y2))


my_array = [2, 1, 0, 8, 15]
a = _max_sub_array(my_array, 0, 4)
print(a)
