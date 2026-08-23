class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=nums.copy()
        b=[]
        for i in nums:
            a.remove(i)
            c=1
            for j in a:
                c*=j
            b.append(c)
            a=nums.copy()
        return b

