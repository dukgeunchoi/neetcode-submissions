class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x < y:
                new = y - x
                heapq.heappush(maxHeap, -new)
            elif x > y:
                new = x - y
                heapq.heappush(maxHeap, -new)
            
        return 0 if len(maxHeap) < 1 else -maxHeap[0]
            

