# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')',
# in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#

class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        struct = {
            '(': {'count': 0, 'indices': []},
            ')': {'count': 0, 'indices': [] }
        }
        for i, c in enumerate(s): 
            if c == '(':
                struct['(']['count'] += 1
                struct['(']['indices'].append(i)
            elif c == ')':
                if struct['(']['count'] > struct[')']['count']:
                    struct[')']['count'] += 1
                    struct['(']['indices'].pop(-1)
                else:
                    struct[')']['indices'].append(i)

        new_s = list(s)
        forb_indices = struct['(']['indices'] + struct[')']['indices']
        for i in forb_indices:
            new_s[i] = '' 
        return ''.join(new_s) 

class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        n_left_p, n_right_p  = 0, 0
        n_left_ind, n_right_ind, new_s  = [], [], []

        for i, c in enumerate(s): 
            if c == '(':
                n_left_p += 1
                n_left_ind.append(i)
                new_s.append('')
            elif c == ')':
                if n_left_p > n_right_p:
                    n_right_p += 1
                    ind = n_left_ind.pop(-1)
                    new_s[ind] = s[ind]
                    new_s.append(c)
                else:
                    n_right_ind.append(i)
                    new_s.append('')
            else:
                new_s.append(c)
        return ''.join(new_s)
 
class Solution3:
    def minRemoveToMakeValid(self, s: str) -> str:
        n_left_p, n_right_p  = 0, 0
        n_left_ind, n_right_ind = [], [] 

        for i, c in enumerate(s): 
            if c == '(':
                n_left_p += 1
                n_left_ind.append(i)
            elif c == ')':
                if n_left_p > n_right_p:
                    n_right_p += 1
                    n_left_ind.pop(-1)
                else:
                    n_right_ind.append(i)

        new_s = list(s)
        for i in n_left_ind + n_right_ind:
            new_s[i] = ''
        return ''.join(new_s)
            

if __name__ == '__main__':
    import time
    import random
    random.seed(314159)
    sol1, sol2, sol3 = Solution1(), Solution2(), Solution3()
    tests = [
        ''.join(
            random.choices(
                ['a','(', ')'],
                weights=[0.3, 0.3, 0.4], 
                k=random.randint(1, 20))) for _ in range(100)
    ]
    s_time = time.time()
    for t in tests:
        sol1.minRemoveToMakeValid(t)
    print(f'extime for sol1: {time.time() - s_time}')
    
    s_time = time.time()
    for t in tests:
        sol2.minRemoveToMakeValid(t)
    print(f'extime for sol2: {time.time() - s_time}')

    s_time = time.time()
    for t in tests:
        sol3.minRemoveToMakeValid(t)
    print(f'extime for sol3: {time.time() - s_time}')
