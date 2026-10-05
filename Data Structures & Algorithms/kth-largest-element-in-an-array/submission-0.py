class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]

        heapq.heapify(maxHeap)

        count = 0
        while count < k:
            n = -heapq.heappop(maxHeap)
            count += 1
            if count == k:
                return n