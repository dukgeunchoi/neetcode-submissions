class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distMap = defaultdict(list)
        distHeap = []

        for x in points:
            d = math.sqrt((x[0] - 0)**2 + (x[1] - 0)**2)
            distMap[d].append(x)
            distHeap.append(d)
        
        heapq.heapify(distHeap)

        print(distHeap, distMap)
        points = []
        while len(points) != k:
            d = heapq.heappop(distHeap)
            p = distMap[d].pop()
            points.append(p)
        
        return points
        