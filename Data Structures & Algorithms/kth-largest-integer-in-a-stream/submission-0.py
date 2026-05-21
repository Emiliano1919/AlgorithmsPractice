class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #Need to practice this one, this one was just for learning 
        #the data structure in python.
        self.minHeap=nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>k:
            #We keep only the last k elements so we always have the kth largest
            #We need to delete the rest, we dont need them
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>self.k:
            #We delete the rest as we are only keeping the kth largest one (it is the top the minimum of the k array)
            heapq.heappop(self.minHeap)
        return self.minHeap[0] #We are always maintaining at the top the important one
