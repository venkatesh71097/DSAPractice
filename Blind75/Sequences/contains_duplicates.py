class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val_set = set()
        for i in nums:
            if i not in val_set:
                val_set.add(i)
            else:
                return True
        return False
