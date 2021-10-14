
class Solution:
    def TwoSum(nums :list[int],target:int) -> list[int]:
        for index,num in enumerate(nums):
            subtract=target-num
            if subtract in nums and nums[index]!=subtract:
                return [index, nums.index(subtract)]

print(Solution.TwoSum(nums=[1,5,4,3,2,1,3,6],target=5))
