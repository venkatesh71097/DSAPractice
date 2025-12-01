class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            res[i] *= left
            left = left * nums[i]

        for j in range(len(nums)-1, -1, -1):
            res[j] *= right
            right = right * nums[j]
        return res
        """
        # Experiments: 
            a) 2 lists to track forward mult and reverse mult
            b) 1 list, but use the same list for accumulating products
            
            # forward_mult = [1] * len(nums)
            # reverse_mult = [1] * len(nums)
            res = [1] * len(nums)
            #[1, 1, 2, 6]
            for i in range(1, len(nums)):
                res[i] = nums[i-1] * res[i-1]
            #[24, 12, 4, 1]
            right = 1
            for j in range(len(nums)-1, -1, -1):
                res[j] *= right
                right *= nums[j]
            #[24, 12, 8, 6] - used zip to do a dot product
            # return [x*y for x, y in zip(forward_mult, reverse_mult)]
            return res

        """