def heapify(arr,n,i):
    largest = i
    left = 2*i
    right = 2*i +1
    if left <=n and arr[largest]<arr[left]:
        largest = left
    if right <=n and arr[largest]<arr[right]:
        largest = right   
    if largest!=i:
        temp = arr[largest]
        arr[largest]= arr[i]
        arr[i]=temp    
        heapify(arr,n,largest)
def heapsort(arr,n):
    while n>1:
        temp = arr[n]
        arr[n]=arr[1]
        arr[1]= temp
        n-=1
        # print(arr)

        heapify(arr,n,1)
        # print("after",arr)zdjkdjksk

arr =[-1,54,53,55,52,50]
n = len(arr)-1
for i in range(n//2+1,0,-1):
    heapify(arr,n,i)

print(arr)
heapsort(arr,n)
print(arr)
