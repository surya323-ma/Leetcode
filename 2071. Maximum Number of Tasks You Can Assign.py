You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.
#code here
 class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort(reverse=True)

        def can_solve(k: int) -> bool:
            w = 0
            p = pills
            q = deque[int]()
            for t in range(k - 1, -1, -1):
                if len(q) == 0 and workers[w] >= tasks[t]:
                    w += 1
                    continue
                if len(q) > 0 and q[0] >= tasks[t]:
                    q.popleft()
                    continue
                while w < k and workers[w] + strength >= tasks[t]:
                    q.append(workers[w])
                    w += 1
                if len(q) > 0 and p > 0:
                    q.pop()
                    p -= 1
                    continue
                return False
            return True

        left, right = 0, min(len(tasks), len(workers))
        closest = 0
        while left <= right:
            mid = (left + right) // 2
            if can_solve(mid):
                closest = mid
                left = mid + 1
            else:
                right = mid - 1

        return closest
