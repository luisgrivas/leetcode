"""
You are given two integer arrays of equal length target and arr.
In one step, you can select any non-empty subarray of arr and reverse it.
You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.
"""
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq_target, freq_arr = {}, {}
        for t in target:
            freq_target[t] = freq_target.get(t, 0) + 1
        for a in arr:
            freq_arr[a] = freq_arr.get(a, 0) + 1
        return freq_target == freq_arr
