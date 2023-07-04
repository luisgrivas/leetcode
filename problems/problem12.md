# 12. Integer to Roman
[Problem](https://leetcode.com/problems/integer-to-roman/description/). Given an integer, convert it to a roman numeral.

🤢

```c++
class Solution {
public:
    string intToRoman(int num) {
        unordered_map<int, string> int2rom = {
            {1, "I"}, {5, "V"}, {10, "X"}, {50, "L"},
            {100, "C"}, {500, "D"}, {1000, "M"}
        };
        string roman = "";
        int base = 1;

        while(base <= num){
            int q = num / base;
            int digit = (q % 10) * base;
            if(digit <= 3 * base ) {
                for(int i = 1; i <= digit / base; i++) {
                    roman = int2rom[base] + roman;
                }
            }else if(digit == 4 * base) {
                roman = int2rom[base] + int2rom[base * 5] + roman;
            } else if(digit == 5 * base) {
                roman = int2rom[base * 5] + roman;
            } else if(digit <= 8 * base) {
                for(int i = 1; i <= (digit / base) - 5; i++) {
                    roman = int2rom[base] + roman;
                }
                roman = int2rom[base * 5] + roman;
            } else {
                roman = int2rom[base] + int2rom[base * 10] + roman;
            }
            base = base * 10;
        }
        return roman;
    }
};
```
