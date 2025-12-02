class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count_dict = dict(Counter(nums))
        # To get key-based sorting, don't put anything in key. with dict.get, you're sorting based on vals. 
        return sorted(count_dict.keys(), key=count_dict.get, reverse=True)[:k]
        # Aliter:
        # iterate thru nums, get a dictionary of unique elements and their frequencies - repetition of counter and then
