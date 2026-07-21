import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.heap = []
        self.added = set()

    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.added.remove(num)
            return num

        self.curr += 1
        return self.curr - 1

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)