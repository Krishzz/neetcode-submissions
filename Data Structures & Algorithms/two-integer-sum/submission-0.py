class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matchs = {}
        for num in range(len(nums)):
            diff = target - nums[num]
            if diff in matchs:
                return [matchs[diff], num]
            matchs[nums[num]] = num
        return -1