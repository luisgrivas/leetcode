# Permutations

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = list()
        
        def tree(current, options):
            if options:
                for ind, val in enumerate(options):
                    new_options = options[:ind] + options[(ind + 1):]
                    tree(current + [val], new_options)
            else:
                permutations.append(current)
                return
        
        tree([], nums)

        return permutations
    
    
    def permute2(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n == 1:
            return [nums]
        elif n == 2:
            return [nums, list(reversed(nums))]
        else:
            half = n  // 2
            perms1 = self.permute2(nums[:half])
            perms2 = self.permute2(nums[half:])
            permutations = list()

            for p in perms1:
                for q in perms2:
                    m = len(q) + 1
                    for i in range(m):
                        permutations.append(q[:i] + p + q[i:])
            
            return permutations
        
    
    def permute3(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n == 1:
            return [nums]
        elif n == 2:
            return [nums, list(reversed(nums))]
        else:
            el = nums[0]
            perms = self.permute3(nums[1:])
            permutations = list()
            for p in perms:
                for i in range(len(p) + 1):
                    q = p.copy()
                    q.insert(i, el)
                    permutations.append(q)
            return permutations
        

if __name__ == '__main__':
    import time
    solution = Solution()

    st = time.process_time()

    for i in range(6):
        nums = list(range(i+1))
        s = solution.permute(nums)
        if len(nums) < 4:
            print(s)
    
    for i in range(10):
        nums = list(range(i, i + 6))
        s = solution.permute(nums)

    et = time.process_time()
    print(et - st)

    print('-'*20, '\n')
    st = time.process_time()

    for i in range(6):
        nums = list(range(i+1))
        s = solution.permute3(nums)
        if len(nums) < 4:
            print(s)
    
    for i in range(10):
        nums = list(range(i, i + 6))
        s = solution.permute3(nums)
    
    et = time.process_time()
    print(et - st)


    print('-'*20, '\n')
    st = time.process_time()

    for i in range(6):
        nums = list(range(i+1))
        s = solution.permute2(nums)
        if len(nums) < 4:
            print(s)
    
    for i in range(10):
        nums = list(range(i, i + 6))
        s = solution.permute2(nums)
    
    et = time.process_time()
    print(et - st)