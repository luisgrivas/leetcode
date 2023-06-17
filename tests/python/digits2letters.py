class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit2letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                        "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                        "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                        "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        letters = [digit2letters.get(digit).copy() for digit in digits ]
        combs = []
        while letters:
            block = letters.pop(0)
            tmp = []
            while block:
                if combs:
                    add = block.pop(0)
                    tmp += [el + add for el in combs]
                else:
                    tmp += block
                    block.clear()
            combs = tmp

        return combs
    
    def letterCombinationsRec(self, digits: str) -> list[str]:
        digit2letters = {"2": "abc", "3": "def",  "4": "ghi",
                        "5": "jkl",  "6": "mno", "7": "pqrs",
                        "8": "tuv", "9": "wxyz"}
        
        if digits == "":
            return []
        elif len(digits) == 1:
            return list(digit2letters.get(digits))
        else:
            first = digits[0]
            rest = digits[1:]
            rec = self.letterCombinationsRec(rest)
            output = []
            for el in digit2letters.get(first):
                output += [ el + val for val in rec]
            return output
        
                

if __name__ == '__main__':
    sol = Solution()

    test = ["234", "23", "", "2", "9", "67", "22"]
    for t in test:
        print(t)
        print(sol.letterCombinationsRec(t))
        print(sol.letterCombinations(t))