# 49. Group Anagrams

[Problem](https://leetcode.com/problems/group-anagrams/). Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

The solution involves ordering the strings to identify anagrams and storing them in a hash map.

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i, s in enumerate(strs):
            sortStr = "".join(sorted(s))
            if sortStr not in hmap:
                hmap[sortStr] = [strs[i]]
            else:
                hmap[sortStr].append(strs[i])
        
        return [hmap[el] for el in hmap] # Or return hmap.values()
```