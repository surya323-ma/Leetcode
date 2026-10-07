Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

 class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string): 
            balance = 0 
            for char in string: 
                if char == '(': balance += 1 
                elif char == ')': balance -= 1 
                if balance < 0: 
                    return False 
            return balance == 0
        queue = deque([s]) 
        visited = set([s]) 
        found = False 
        result = [] 
        while queue: 
            current = queue.popleft() 
            if isValid(current): 
                result.append(current) 
                found = True 
            if found:
                continue
            for i in range(len(current)): 
                if current[i] not in ('(', ')'): 
                    continue 
                next_state = current[:i] + current[i+1:] 
                if next_state not in visited: 
                    visited.add(next_state) 
                    queue.append(next_state) 
        return result
