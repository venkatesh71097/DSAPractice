class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # Getting the index and number so that I can get a hashmap
        # corresponding to index & number in that index of list
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap: 
                # Hashmap will have only the visited elements' values
                # hashmap[complement] will give the index of that complement value
                return [i, hashmap[complement]]
            hashmap[n] = i
        return []