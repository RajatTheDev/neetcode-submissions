class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # edge case handled here
        if len(strs) <= 1:
            return [strs]

        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())