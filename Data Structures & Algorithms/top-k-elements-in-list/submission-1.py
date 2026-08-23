class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=[]
        x=[]
        for i in set(nums):
            c=0
            for j in nums:
                if i==j:
                    c+=1
            a.append([c,i])
        b=sorted(a)[::-1]
        if len(b)==1:
            return ([b[0][1]])
        else:
            d=b[:k]
            for i in d:
                x.append(i[1])
            return x
