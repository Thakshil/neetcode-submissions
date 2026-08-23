class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for ind,val in enumerate(nums):
            match=target-val
            if match in a:
                return [a[match],ind]
            a[val]=ind