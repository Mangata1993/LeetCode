class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count = collections.Counter(tasks)
        # max_freq = max(count.values())
        # item = 0
        # for val in count.values():
        #     if val == max_freq:
        #         item += 1
        # return max((max_freq - 1) * (n + 1) + item, len(tasks))
        freqs = [0] * 26
        for char in tasks:
            freqs[ord(char) - ord('A')] += 1
        freqs.sort(reverse = True)
        idle = (freqs[0] - 1) * n
        for freq in freqs[1:]:
            if idle > 0:
                idle -= min(freqs[0] - 1, freq)
        return len(tasks) + max(0, idle)
