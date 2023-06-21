class Solution:
    """Al parecer esto si funciona..."""
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            n = -n 
            x = 1 / x
        
        rest = self.myPow(x, n // 2)
        if n % 2 == 0:
            return rest * rest
        
        return x * rest * rest 

if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(3.0, 2))