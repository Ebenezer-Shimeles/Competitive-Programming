class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        popped_ptr: int = 0
        stack: list = []

        for elem in pushed:
            stack.append(elem)
            while len(stack) != 0 and popped[popped_ptr] == stack[-1]:
                stack.pop(-1)
                popped_ptr +=1
        
        return len(stack) == 0
