class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in dict:
                dict[nums[i]]=i
            else:
                return [dict[difference],i]
          
        