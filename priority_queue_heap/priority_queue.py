import heapq

# Creating a max heap
max_heap = []
data = [4, 2, 5, 3]
heapq._heapify_max(data)

# for item in data:
#     heapq.heappush(max_heap, -item)  # Use negative values to create a max heap

# Get the maximum element (equivalent to pq.top() in C++)
max_element = data[0]
print("Element at Top:", max_element)

# Pop the maximum element (equivalent to pq.pop() in C++)
print(heapq._heappop_max(data))

# Get the new maximum element
new_max_element = data[0]
print("Element at Top:", new_max_element)