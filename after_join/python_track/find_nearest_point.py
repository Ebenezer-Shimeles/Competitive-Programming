import math

class Solution:
    def distance(self, x1, x2, y1, y2):
        return abs(x2 -x1) + abs(y2-y1)

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest = float('inf')
        smallest_index = 0

        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                 distance =  self.distance(x, point[0], y, point[1])
                 if smallest > distance:
                     smallest = distance
                     smallest_index = i
                 print(f'smallest = {smallest}, points = {point}')
        return smallest_index if not math.isinf(smallest) else -1