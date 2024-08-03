"""
You are given a 0-indexed integer array nums containing distinct numbers, an integer start,
and an integer goal. There is an integer x that is initially set to start, and you want
to perform operations on x such that it is converted to goal.
You can perform the following operation repeatedly on the number x:

If 0 <= x <= 1000, then for any index i in the array (0 <= i < nums.length), you can set x to any of the following:

* x + nums[i]
* x - nums[i]
* x ^ nums[i] (bitwise-XOR)
Note that you can use each nums[i] any number of times in any order.
Operations that set x to be out of the range 0 <= x <= 1000 are valid, but no more operations can be done afterward.

Return the minimum number of operations needed to convert x = start into goal, and -1 if it is not possible.
"""

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        return 0

def dp(x: int, goal: int, nums: list[int], hash: dict):
    if goal in hash:
        return hash[goal]
    if x == goal:
        hash[goal] = 0
    elif x > 1000:
        return float('inf')
    else:
        min_ops = float('inf') 
        for num in nums:
            min_ops = min(
                min_ops,
                dp(x + num, goal + num, nums, hash),
                dp(x - num, goal - num, nums, hash),
                dp(x^num, goal^num, nums, hash)
                )
        hash[goal] = min_ops + 1
    return hash[goal] 

from collections import deque

def bfs(x: int, goal: int, nums: list[int]):
    visited = {x: 0} 
    stack = deque([x])
    while stack:
        x = stack.popleft()
        if x == goal:
            return visited[x]
        elif 0 <= x <= 1000:
            count = visited[x] + 1
            for num in nums:
                x_ = x + num
                visited[x_] = visited.get(x_, count) 
                stack.append(x_)
    return -1


def bfs(x: int, goal: int, nums: list[int]): #NOTE: SLOWWW!!!
    visited = {x}
    stack = deque([[x, 0]])
    while stack:
        [x, c] = stack.popleft()
        if x == goal:
            return c
        if 0 <= x <= 1000:
            c_ = c + 1
            for num in nums:
                if (x_ := x + num) not in visited:
                    stack.append([x_, c_] )
                    visited.add(x_)
                if (x_ := x - num) not in visited:
                    stack.append([x_, c_] )
                    visited.add(x_)
                if (x_ := x^num) not in visited:
                    stack.append([x_, c_] )
                    visited.add(x_)
    return -1
