# Given an integer array nums of length n where all the integers
# of nums are in the range [1, n] and each integer appears once or twice, 
# return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant 
# extra space.
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_map = {num:0 for num in nums}
        for num in nums:
            hash_map[num] += 1
        duplicates = []
        for num, count in hash_map.items():
            if count > 1:
                duplicates.append(num)
        return duplicates


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                duplicates.append(num)
            nums[num - 1] *= -1
        return duplicates


if __name__ == '__main__':
    sol = Solution()
    # nums = [2,2,3]
    # nums = [3,1,4,4,1,2]
    # nums = [4,3,2,7,8,2,3,1]
    # nums = [39,31,8,14,14,38,5,15,29,49,18,6,30,47,8,35,2,17,6,10,29,46,41,48,1,36,5,28,46,39,7,47,18,42,17,11,36,45,21,33,24,10,24,50,25,16,9,12,11,25]
    print(sol.findDuplicates(nums))


# nums = [3,1,4,4,1,2]
# nums = [4, 1, -1, 4, 1, 2]
# nums = [-1, 4, -1, 4, 1, 2]
# nums = [-1, 4, -1, 4, 1, 2]
# nums = [-1, 4, -1, -1, 1, 2]
# nums = [-1, 4, -1, -1, 1, 2]
# nums = [-1, -1, -1, -1, 1, 4]


# nums = [2,2,3]
# nums = [2, -1 , 3]
# nums = [2, -1 , -1]
