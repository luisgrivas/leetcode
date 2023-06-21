# 30. Substring with Concatenation of All Words

[Problem.](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) You are given a string s and an array of strings words. All the strings of words are of the same length.

```python
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        counts = collections.Counter(words)
        k = len(s)
        m = len(words[0])
        n = len(words)
        length = m * n
        indices = list()

        for ind in range(k - length + 1):
            parts = list()
            for jnd in range(ind, ind + length, m):
                parts.append(s[jnd:(jnd + m)])

            second_counts = collections.Counter(parts)
        
            if counts == second_counts:
                indices.append(ind)

        return indices 
```

```c++
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        bool flag = true;
        int string_length = s.size(), words_list_length = words.size();
        int word_length = words[0].size(), substr_length = word_length * words_list_length;
        vector<int> indices;
        unordered_map<string, int> word_counts, substr_counts;

        for(auto w: words) word_counts[w]++;

        for(int ind = 0; ind < string_length - substr_length + 1; ind++){
            substr_counts = word_counts;
            for(int jnd = ind; jnd < ind + substr_length; jnd += word_length ){
                string sbstr = s.substr(jnd, word_length);
                if(substr_counts.count(sbstr)){
                    if(substr_counts[sbstr] > 0){
                    substr_counts[sbstr] -= 1;
                    }
                    else{
                        flag = false;
                        break;
                    }
                }else{
                    flag = false;
                    break;
                }
            }
            if(flag){
                indices.push_back(ind);
            }
            flag = true;
            substr_counts.clear();
        }
        return indices;
    }
};
```