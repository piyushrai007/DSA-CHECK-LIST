def compression_first(s):
    a = ""
    a += s[0]
    for i in range(1, len((s))):
        cur = s[i]
        prev = s[i-1]
        print(cur, prev)
        if cur != prev:
            a += cur
    return a


def compression_second(s):
    a = ""
    a += s[0]
    count = 1
    for i in range(1, len((s))):
        cur = s[i]
        prev = s[i-1]
        if cur == prev:
            count += 1
        else:
            if count > 1:
                a += str(count)
                count = 1
            a += cur
    if count > 1:     
        a += str(count)
    return a


s = "aaabbbcccddaeef"
print(compression_first(s))
print(compression_second(s))
