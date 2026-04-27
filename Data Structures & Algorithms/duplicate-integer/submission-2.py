class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # print(len(nums), len(set(nums)))
        collect = set()
        for num in nums:
            if num in collect:
                return True
            collect.add(num)
        return False

        # return len(nums) != len(set(nums))
