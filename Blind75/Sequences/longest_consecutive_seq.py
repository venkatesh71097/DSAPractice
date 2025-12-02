class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Just get the unique elements, run over a for loop and then try to find sequences without breaks
        # If there is a break, reset the length counter to 1 and then go over a while loop to find consecutive elements that are found in the list/set
        max_length = 0
        unique_nums= set(nums)
        for i in unique_nums:
            if (i-1) not in unique_nums:
                length = 1
                while i+length in unique_nums:
                    length += 1
                max_length = max(length, max_length)
        return max_length
