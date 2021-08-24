class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        count = collections.Counter(nums)
        for key, val in count.items():
            buckets[val].append(key)
        # print(buckets, *buckets)
        return list(chain(*buckets))[-k:]
