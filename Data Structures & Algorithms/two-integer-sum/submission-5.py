class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i,n in enumerate(nums):
            value = target - n
            if value in dict1:
                return [dict1[value], i]
            else:
                dict1[nums[i]] = i

