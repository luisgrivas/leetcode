class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"(": ")", "[": "]", "{": "}"}
        tmp  = []
        for ch in s:
            if ch in parentheses:
                tmp.append(ch)
            elif tmp and parentheses[tmp[-1]] == ch:
                tmp.pop()
            else:
                return False
        return not tmp

if __name__ == '__main__':
    tests = ["()", "()[]{}", "(]", "]}{[", "(", "({[([[]])]})", "({[([[{]])]})",
             "({)}", "([()])[{()}]"]
    vals = [True, True, False, False, False, True, False, False, True]
    sol = Solution()
    flag = 0
    for i,t in enumerate(tests):
        val = sol.isValid(t)
        if val != vals[i]:
            flag+=1
            print("Not valid answer for case: ", t)
    
    if flag == 0:
        print("All cases passed.")
