import heapq
sample_list = [1,12,33,24,65,46,78,58,39,710,41,128,159, 345, 154]

# h = []
# for item in sample_list:
#     heapq.heappush(h, item)
# print(heapq.nlargest(3, h))

heapq.heapify(sample_list)
print(heapq._heappop_max(sample_list))

