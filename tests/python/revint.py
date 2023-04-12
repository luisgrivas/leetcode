class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sig = 1
        liminf = -214748364.8
        limsup = 214748364.7
        if x < 0:
            x = -x
            sig = -1
        while(x >= 1):
            r = x % 10
            if sig*rev > limsup - r/10 or sig*rev < liminf - r/10:
                rev = 0
                x = 0
            else:
                rev = (rev * 10) + r
                x = int(x / 10)
        return rev*sig



if __name__ == '__main__':
    cases = [0, -1, 1, 100, -200, -2**31, -147483648,
            -2147483640, 2147483647, 2147483640, -201, 3981 ]
    sol = Solution()
    for c in cases:
        print("input: {}".format(c), "\noutput: {}\n".format(sol.reverse(c)))