# 1. Two Sum

[Problem.](https://leetcode.com/problems/two-sum/description/) Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.


One has to find all posible combinations of the form $(x_i, x_j)$ where $i < j$ and compute $x_i + x_j$. This can be done with two nested foor loops.

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indices;
        for(int i = 0; i < nums.size() - 1; i++) {
            for(int j = i + 1; j < nums.size(); j++) {
                int sum = nums.at(i) + nums.at(j);
                if(sum == target){
                    indices = {i, j};
                }
            }
        }
        return indices;
    }
};
```
