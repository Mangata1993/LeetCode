class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        already_satisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
                customers[i] = 0
        
        current_satisfied = 0
        max_satisfied = 0
        for i in range(len(customers)):
            current_satisfied += customers[i]
            if i >= X:
                current_satisfied -= customers[i - X]
            max_satisfied = max(max_satisfied, current_satisfied)  #这句话必须加在if外面，因为有可能i<X，但也得有结果
        
        return already_satisfied + max_satisfied
    
    
