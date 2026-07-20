class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # edge case handled here
        if len(strs) <= 1:
            return [strs]

        res = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                arr[index] += 1
            res[tuple(arr)].append(s)
        return list(res.values())