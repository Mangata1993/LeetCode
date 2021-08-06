class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free_servers = [(weight, index, 0) for index, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        inuse_servers = []
        res = []
        # available_time, weight, index
        for i, time in enumerate(tasks):
            while inuse_servers and inuse_servers[0][0] <= i or not free_servers:
                available_time, weight, index = heapq.heappop(inuse_servers)
                heapq.heappush(free_servers, (weight, index, available_time))
            weight, index, available_time = heapq.heappop(free_servers)
            res.append(index)
            heapq.heappush(inuse_servers, (max(i, available_time) + time, weight, index))
        return res
