class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        ln = len(nums)
        for i in range(ln):
            ls = nums[:i]+nums[i+1:ln]
            nums.append(self.productList(ls))
        return nums[ln:]
    
    def productList(self, lst, product=1):
        ar = [product:= product*x for x in lst]
        return product
        