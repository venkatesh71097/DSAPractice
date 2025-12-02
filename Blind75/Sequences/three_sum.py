class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      # Sort the numbers, ensure that there are 0 duplications of numbers in the triplet, and then have these 2 nos. fixed so that you can negative multiply -1 to the sum of these 2. 
      # If that negated number is in the subsequent elements of the list (not in the past), you're good! That's your triplet. 
        nums.sort()
        result = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                third = (n + nums[j]) * -1
                if third in nums[j+1:]:
                    triplet = [n, nums[j], third]
                    if triplet not in result:
                        result.append(triplet)
        return result
