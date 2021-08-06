class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available_task = [(enqueue, processing, index) for index, (enqueue, processing) in enumerate(tasks)]
        heapq.heapify(available_task)   # 这里不能用heapify,只能用sorted(为了保证每一项都有序)
        task_in_progress = []
        res = []
        time = available_task[0][0]
        i = 0
        while len(res) < len(tasks):
            while i < len(tasks) and available_task[i][0] <= time:
                heapq.heappush(task_in_progress, (available_task[i][1], available_task[i][2]))
                i += 1
            if task_in_progress:
                processing, index = heapq.heappop(task_in_progress)
                time += processing
                res.append(index)
            else:
                time = available_task[i][0]
        return res
    
    
        
