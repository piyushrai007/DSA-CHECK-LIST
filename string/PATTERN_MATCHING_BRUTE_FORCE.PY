def strstr(haystack, needle):
        i = 0
        j = 0
        n = len(haystack)
        m = len(needle)
        
        if haystack == needle:
            return 0
        
        while i < n:
            if haystack[i] == needle[j]:
                index = i
                temp = ""
                while i < n and j < m and haystack[i] == needle[j]:
                    temp += haystack[i]
                    i += 1
                    j += 1
                if temp == needle:
                    return index,index+j
                else:
                    i = index + 1
                    j = 0
            else:
                i += 1
        
        return -1
a = "piyushraivdsoops"
b="ush"
c,d = strstr(a,b)
print(c,d,a[c:d])