class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sums = []
        for i in range(1, len(nums)):
            sums = [x+y for x,y in zip(nums, nums[i:] + nums[:i])]
            if target in sums:
                return [sums.index(target), (sums.index(target) + i)%len(nums)]
            
        