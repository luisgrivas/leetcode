class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        count = 1
        for ind in range(len(digits) - 1, -1, -1):
            if count == 0: break

            total = digits[ind] + count
            digits[ind] = total % 10
            count = total // 10

        if count > 0:
            digits.insert(ind, 1)
        return digits 

    def plusOne2(self, digits: list[int]) -> list[int]:
        count = 1
        new_digits = list()
        for el in reversed(digits):
            if count == 0:
                new_digits.append(el)
            else:
                total = el + count
                new_digits.append(total % 10)
                count = total // 10
        
        if count > 0: new_digits.append(1)
        return list(reversed(new_digits)) 
    
    def plusOne3(self, digits: list[int]) -> list[int]:
        count = 1
        n = len(digits) - 1
        for ind, el in enumerate(reversed(digits)):
            if count == 0: break
            total = el + count
            digits[n - ind] = total % 10
            count = total // 10
        
        if count > 0: digits.insert(n - ind, 1)

        return digits

    def plusOne4(self, digits: list[int]) -> list[int]:
        count = 1
        n = len(digits) - 1
        for ind, el in enumerate(reversed(digits)):
            if count == 0: break
            total = el + count
            if total == 10: digits[n - ind] = 0
            else: digits[n - ind] = total; count = 0
        
        if count > 0: digits.insert(n - ind, 1)

        return digits
    
    def plusOne5(self, digits: list[int]) -> list[int]:
        count = 1
        for ind in reversed(range(len(digits))):
            if count == 0: break
            digits[ind] += count
            count = digits[ind] // 10
            digits[ind] %= 10 

        if count > 0:
            digits.insert(0, 1)
        return digits



if __name__ == '__main__':
    import time 
    solution = Solution()

    st = time.process_time()
    digits = [1,2,3]
    print(solution.plusOne(digits))

    digits = [4,3,2,1]
    print(solution.plusOne(digits))

    digits = [9]
    print(solution.plusOne(digits))

    digits = [9,9,9]
    print(solution.plusOne(digits))
    
    digits = [9,0,9]
    print(solution.plusOne(digits))

    digits = [1,9]
    print(solution.plusOne(digits))

    digits = [9,9]
    print(solution.plusOne(digits))


    et = time.process_time()
    print(et - st)

    print('-'*10)
    st = time.process_time()
    digits = [1,2,3]
    print(solution.plusOne2(digits))

    digits = [4,3,2,1]
    print(solution.plusOne2(digits))

    digits = [9]
    print(solution.plusOne2(digits))

    digits = [9,9,9]
    print(solution.plusOne2(digits))
    
    digits = [9,0,9]
    print(solution.plusOne2(digits))

    digits = [1,9]
    print(solution.plusOne2(digits))

    digits = [9,9]
    print(solution.plusOne2(digits))

    et = time.process_time()
    print(et - st)


    print('-'*10)
    st = time.process_time()
    digits = [1,2,3]
    print(solution.plusOne3(digits))

    digits = [4,3,2,1]
    print(solution.plusOne3(digits))

    digits = [9]
    print(solution.plusOne3(digits))

    digits = [9,9,9]
    print(solution.plusOne3(digits))
    
    digits = [9,0,9]
    print(solution.plusOne3(digits))

    digits = [1,9]
    print(solution.plusOne3(digits))

    digits = [9,9]
    print(solution.plusOne3(digits))

    et = time.process_time()
    print(et - st)



    print('-'*10)
    st = time.process_time()
    digits = [1,2,3]
    print(solution.plusOne4(digits))

    digits = [4,3,2,1]
    print(solution.plusOne4(digits))

    digits = [9]
    print(solution.plusOne4(digits))

    digits = [9,9,9]
    print(solution.plusOne4(digits))
    
    digits = [9,0,9]
    print(solution.plusOne4(digits))

    digits = [1,9]
    print(solution.plusOne4(digits))

    digits = [9,9]
    print(solution.plusOne4(digits))

    et = time.process_time()
    print(et - st)



    print('-'*10)
    st = time.process_time()
    digits = [1,2,3]
    print(solution.plusOne5(digits))

    digits = [4,3,2,1]
    print(solution.plusOne5(digits))

    digits = [9]
    print(solution.plusOne5(digits))

    digits = [9,9,9]
    print(solution.plusOne5(digits))
    
    digits = [9,0,9]
    print(solution.plusOne5(digits))

    digits = [1,9]
    print(solution.plusOne5(digits))

    digits = [9,9]
    print(solution.plusOne5(digits))

    et = time.process_time()
    print(et - st)