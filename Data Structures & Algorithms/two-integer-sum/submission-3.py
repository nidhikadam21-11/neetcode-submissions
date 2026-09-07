class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}

        for i in range(len(nums)):
            value = target - nums[i]
            if value in dict1:
                return [dict1[value], i]
            else:
                dict1[nums[i]] = i

