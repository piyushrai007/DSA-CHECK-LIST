def majorityElement( A, N):
        n = len(A)

        hashtable = {}

        for num in A:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1

        for key, value in hashtable.items():
            if value > (n / 2):
                return key

        return -1 
