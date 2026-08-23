class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        x=Counter(nums)
        y = sorted(x.items(), key=lambda item: item[1], reverse=True)
        res=[]
        for i in range(k):
            res.append(y[i][0])
        return res