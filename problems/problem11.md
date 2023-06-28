# 11. Container With Most Water

[Problem](https://leetcode.com/problems/container-with-most-water/description/). You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.


The naive solution involves calculating the area for all possible pairs of elements in the height array, resulting in a time complexity of $O(n^2)$. To optimize this, we can use a two-pointer approach. We initialize one pointer at the beginning of the array and the other at the end. In each iteration, we calculate the area and move the pointer pointing to the lower height. We update a variable if we find a larger area.

Here are the Python and c++ implementations: 

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        right = len(height) - 1
        left = 0
        area = 0
        while left < right:
            leftValue = height[left]
            rightValue = height[right]
            if leftValue < rightValue:
                newArea = leftValue * (right - left)
                left += 1
            else:
                newArea = rightValue * (right - left)
                right -= 1
            
            if newArea > area:
                area = newArea

        return area
```

```c++
class Solution {
public:
    int maxArea(vector<int>& height) {
    int left = 0, right = height.size() - 1, area = 0, newArea;
    while(left < right){
        int leftValue = height.at(left);
        int rightValue = height.at(right);
        if(leftValue < rightValue){
            newArea = leftValue * (right - left);
            left += 1;
        }else{
            newArea = rightValue * (right - left);
            right -= 1;
        }
        if(newArea > area){
            area = newArea;
        }
    }
    return area;
        
    }
};
```