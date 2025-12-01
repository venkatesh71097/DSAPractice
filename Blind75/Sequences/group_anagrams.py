class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from colllections import defaultdict
        ctr = defaultdict(list)
        for i in strs:
            ctr[tuple(sorted(i))].append(i)
        print(ctr)
        return list(ctr.values())

        """
        Aliter: 
            for s in strs:
                count = [0] * 26
                for c in s:
                    count[ord('c') - ord('a')] += 1 #ASCII Correction performed to get the indices from 0 to 25
                a[tuple(count)].append(s) # to hash it, we need to convert list to tuple as lists are unhashable. 
                # Hashable types: int, float, string, tuple as they are immutable.
            return list(a.values())
        """