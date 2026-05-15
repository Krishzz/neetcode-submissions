class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = 0
        l2 = 0
        r1 = len(nums1)
        r2 = len(nums2)
        arr = []
        while l1<r2:
            l2 = 0
            while l2<r2:
                if nums1[l1] == nums2[l2]:
                    arr.append(l2)
                    break
                l2+=1
            l1+=1
        return arr