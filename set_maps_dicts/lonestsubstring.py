def substring(s):
    dict = {s[i]:-1 for i in range(0,len(s))}

    maxline = 0
    start =-1
    for i in range(0,len(s)):
        if dict[s[i]]>start:
            start = dict[s[i]]
        dict[s[i]] = i
        maxline = max(maxline,i-start)
    return maxline
a="abcabc"
print(substring(a))