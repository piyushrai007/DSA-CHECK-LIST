import heapq

class MedianOfAStream:
    def __init__(s):
        s.minHeap = [ ]
        s.maxHeap = [ ]
    
    def insertNum(s, num):
        if len(s.maxHeap) == 0 or num <= s.maxHeap[-1]:
            heapq.heappush(s.maxHeap, num)
        else:
            heapq.heappush(s.minHeap, num)

        if len(s.maxHeap) > len(s.minHeap) + 1:
            heapq.heappush(s.minHeap, heapq.heappop(s.maxHeap))
        elif len(s.maxHeap) < len(s.minHeap):
            heapq.heappush(s.maxHeap, heapq.heappop(s.minHeap))
        print("max",s.maxHeap)
        print("min",s.minHeap)

    def findMedian(s):
        if len(s.maxHeap) == len(s.minHeap):
            return (s.maxHeap[-1] + s.minHeap[0]) / 2.0
        else:
            return s.maxHeap[-1]
        

m = MedianOfAStream()
m.insertNum(1)
m.insertNum(2)
m.insertNum(3)
# m.insertNum(4)
print(m.findMedian())
