class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return [key for key in sorted(counter.keys(), key=lambda x: counter[x], reverse=True)][:k]