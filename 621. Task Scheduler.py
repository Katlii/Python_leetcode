"""Given a characters array tasks, representing the tasks a CPU needs to do,
where each letter represents a different task. Tasks could be done in any order.
Each task is done in one unit of time. For each unit of time,
the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents
the cooldown period between two same tasks (the same letter in the array),
that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish
all the given tasks.
"""

from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        max_tasks = sum(1 for count in task_counts.values() if count == max_count)
        intervals_needed = (max_count - 1) * (n + 1) + max_tasks
        return max(intervals_needed, len(tasks))


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n=2
print(Solution().leastInterval(tasks, n))
