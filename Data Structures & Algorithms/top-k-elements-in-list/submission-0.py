class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for n in nums:
            # creating key n if it does not exist and storing frequencies
            hashMap[n] = hashMap.get(n, 0)+1

        # now I got a descending value hash map
        hashMap = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))
        result = [] * k
        l = k

        for key, value in hashMap.items():
            if l == 0:
                break
            else:
                result.append(key)
                l -= 1

        return result