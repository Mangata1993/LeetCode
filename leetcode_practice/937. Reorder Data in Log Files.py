class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs = [string.split() for string in logs]
        # print(logs)
        letters = [log for log in logs if log[1].isalpha()]
        digits = [log for log in logs if log[1].isdigit()]
        letters.sort(key = lambda x: (x[1:], x[0]))
        return [' '.join(log) for log in (letters + digits)]
    
