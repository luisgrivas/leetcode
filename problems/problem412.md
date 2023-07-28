412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

* answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
* answer[i] == "Fizz" if i is divisible by 3.
* answer[i] == "Buzz" if i is divisible by 5.
* answer[i] == i (as a string) if none of the above conditions are true.

The solution is pretty self-explanatory. I solved this problem mainly for the sake of completeness and not for being particularly interesting. This Python implementation beats ~86% of users in runtime. 

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        base = [str(i) if i % 3 != 0 and i % 5 != 0 else '' for i in range(1,n+1) ]
        threes = ["Fizz" if i % 3  == 0 else '' for i in range(1,n+1)]
        fives = ["Buzz" if i % 5 == 0 else '' for i in range(1, n+1)]
        answer = ["".join(t) for t in zip(base,threes,fives)]

        return answer
````