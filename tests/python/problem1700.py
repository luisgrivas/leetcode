# The school cafeteria offers circular and square sandwiches at lunch break,
# referred to by numbers 0 and 1 respectively. All students stand in a queue.
# Each student either prefers square or circular sandwiches.
#
# The number of sandwiches in the cafeteria is equal to the number of students.
# The sandwiches are placed in a stack. At each step:
#
# If the student at the front of the queue prefers the sandwich on the top of the stack,
# they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
#
# You are given two integer arrays students and sandwiches where sandwiches[i]
# is the type of the ith sandwich in the stack
# (i = 0 is the top of the stack) and students[j] is the preference of the jth
# student in the initial queue (j = 0 is the front of the queue). Return
# the number of students that are unable to eat.


from collections import deque
from typing import List


class Solution1:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = deque(students), deque(sandwiches)
        while sandwiches and sandwiches[0] in students:
            student = students.popleft()
            if student == sandwiches[0]:
                sandwiches.popleft()
            else:
                students.append(student)
        return len(students)

class Solution2:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = deque(students), deque(sandwiches)
        students_preferences = {1: students.count(1), 0: students.count(0)}
        while sandwiches and students_preferences[sandwiches[0]] > 0:
            student = students.popleft()
            if student == sandwiches[0]:
                sandwich = sandwiches.popleft()
                students_preferences[sandwich] -= 1
            else:
                students.append(student)
        return len(students)

class Solution3:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = students[::-1], sandwiches[::-1]
        n, j = len(students), 0
        while sandwiches and j < n:
            student = students.pop()
            if student == sandwiches[-1]:
                sandwiches.pop()
                n -= 1
                j = 0
            else:
                students = [student] + students
                j += 1
        return n

class Solution4:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = students[::-1], sandwiches[::-1]
        n = len(students)
        while sandwiches and sandwiches[0] in students:
            student = students.pop()
            if student == sandwiches[-1]:
                sandwiches.pop()
                n -= 1
            else:
                students = [student] + students
        return n



if __name__ == '__main__':
    import time
    import random
    random.seed(314159)
    sel_tests = [
        {'students':[1,1,1,0,0,1], 'sandwiches': [1,0,0,0,1,1]},
        {'students':[1,1,0,0], 'sandwiches': [0,1,0,1]},
    ]
    solutions = [Solution1(), Solution2(), Solution3()]
    # print(solutions[-1].countStudents(**sel_tests[0]))

        
    # sizes = [ random.randint(1, 20) for _ in range(1000)] 
    sizes = random.choices(list(range(1,20)), k=10000) 
    tests = [
        {
            'students': random.choices([1, 0], k=j),
            'sandwiches': random.choices([1, 0], k=j)
        } for j in sizes
    ]
    for sol in solutions:
        s_time = time.time()
        for t in tests:
            sol.countStudents(**t)
        print(f'Ex time {time.time() - s_time}')
