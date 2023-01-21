class StaticArrays:

    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        # write your code here
        self.capacity = capacity
        self.arr = arr
        self.length = length


    def insertEnd(self, value):
        # write your code here
        if self.length >= self.capacity:
            raise Exception("Error array is full")
        self.arr[self.length-1] = value
        length += 1
       
    def removeEnd(self):
        # write your code here
        if self.length == 0:
            raise Exception("Error array is empty")
        self.length -= 1
    def insertMiddle(self, index, value):
        # write your code here, you need to shift elements after insertion
        if self.length >= self.capacity:
            raise Exception("Error array is full!")
        mid = 0
        for i in range(self.length//2):
            mid = i
        if self.length % 2:
            mid += 1
        
        for i in range(mid,  self.length-1):
             self.arr[i+1] = self.arr[i]
        self.arr[mid] = value
    def removeMiddle(self, index):
        # write your code here, you need to shift elements after removal
        if self.length == 0:
            raise Exception("Error array is empty!")
        mid = 0
        for i in range(self.length//2):
            mid = i
        if self.length % 2:
            mid += 1
        for i in range(mid, self.length - 1):
            self[i] = self[i+1]
        self.length -= 1
    def printArr(self):
        # write your code here
        for i in range(self.length):
            print(self.arr[i], end=', ')