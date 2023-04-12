# 4. Median of Two Sorted Arrays

[Problem.](https://leetcode.com/problems/median-of-two-sorted-arrays/) Given two sorted arrays nums1 and nums2 of size $m$ and $n$ respectively,
return the median of the two sorted arrays. The overall run time complexity should be $O(log (m+n))$.

Notice that we don't need to merge the arrays, since we know that the median is located at index $(m+n)/2$ if $m+n$ is odd, or is the mean of the elements with index $\lfloor(m+n)/2 \rfloor$ and $\lceil(m+n)/2 \rceil$ if $m+n$ is even. So we only merge the arrays until the index $\lceil(m+n)/2 \rceil$ and proceed acordingly. The implementation is ugly, since we have to deal with extreme cases (such as empty arrays, etc). 

```python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = int((m + n) / 2) + 1
        j = 0
        k = 0
        if m == 0:
            merged_arrays = nums2
        elif n == 0:
            merged_arrays = nums1
        else:
            merged_arrays = []
            while j + k != i:
                if j >= m:
                    merged_arrays.append(nums2[k])
                    k+=1
                elif k >= n:
                    merged_arrays.append(nums1[j])
                    j+=1
                elif nums1[j] <= nums2[k]:
                    merged_arrays.append(nums1[j])
                    j+=1
                else:
                    merged_arrays.append(nums2[k])
                    k+=1
                    
        if (m + n) % 2 == 1:
            return merged_arrays[i-1]
        else:
            return (merged_arrays[i-1] + merged_arrays[i-2]) / 2

