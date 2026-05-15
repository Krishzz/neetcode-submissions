class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = 0
        r1 = len(nums1)
        arr = []
        while l1<r1:
            for l2 in range(len(nums2)):
                if nums1[l1] == nums2[l2]:
                    arr.append(l2)
                    break
            l1+=1
        return arr