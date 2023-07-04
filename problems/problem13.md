# 13. Roman to Integer

[Problem](https://leetcode.com/problems/roman-to-integer/description/). Given a roman numeral, convert it to an integer.

TODO: Some explanation

```c++
class Solution {
public:
    std::unordered_map<char, int> roman2int = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000}
        };

    int romanToInt(string s) {
        int current, prev = 0, number = 0;
        for(int i = s.size() - 1; i >= 0; i--) {
            current = roman2int[s[i]];
            if(prev <= current) {
                number += current;
                }
            else {
                number -= current;
                }
            prev = current;
        }
        return(number);
    }
};
```
