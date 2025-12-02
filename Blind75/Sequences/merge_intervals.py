class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Connected components - Qualcomm interview 2021
        # Will do later...
        # Sort + iterate over elements
        intervals.sort(key=lambda x: x[0])
        a = [intervals[0]] # [1,3]
        for start, end in intervals[1:]: 
            # [2, 6]
            if start <= a[-1][1]:
                a[-1][1] = max(end, a[-1][1])
            else:
                a.append([start, end])
        return a