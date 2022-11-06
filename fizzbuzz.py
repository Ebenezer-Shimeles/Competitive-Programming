class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        li : List[str] = []
        for i in range(n):
            index = i + 1
            if index % 15 == 0:
                li.append("FizzBuzz")
            elif index % 3 == 0:
                li.append("Fizz")
            elif index % 5 == 0:
                li.append("Buzz")
            else:
                li.append(str(index))
        return li
        