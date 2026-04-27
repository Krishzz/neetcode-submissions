# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
    #     return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    # def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
    #     if e-s+1<=1:
    #         return pairs
        
    #     m = (e+s)//2

    #     self.mergeSortHelper(pairs, s, m)
    #     self.mergeSortHelper(pairs, m+1, e)

    #     self.merge(pairs, s, e, m)

    #     return pairs
    
    # def merge(self, arr: List[Pair], s: int, e: int, m: int) -> None:
    #     L = arr[s:m+1]
    #     R = arr[m+1: e+1]

    #     i = 0
    #     j = 0
    #     k = s

    #     while i<len(L) and j<len(R):
    #         if L[i].key<=R[j].key:
    #             arr[k] = L[i]
    #             i+=1
    #         else:
    #             arr[k] = R[j]
    #             j+=1
    #         k+=1
        
    #     while i<len(L):
    #         arr[k] = L[i]
    #         i+=1
    #         k+=1
        
    #     while j<len(R):
    #         arr[k] = R[j]
    #         j+=1
    #         k+=1
        



        if len(pairs)<=1:
            return pairs
        
        mid = len(pairs)//2
        left_arr = pairs[:mid]
        right_arr = pairs[mid:]
        self.mergeSort(left_arr)
        self.mergeSort(right_arr)

        lp = rp = fp = 0

        while lp<len(left_arr) and rp<len(right_arr):
            if left_arr[lp].key<=right_arr[rp].key:
                pairs[fp] = left_arr[lp]
                lp+=1
            else:
                pairs[fp] = right_arr[rp]
                rp+=1
            fp+=1
        
        while lp<len(left_arr):
            pairs[fp] = left_arr[lp]
            lp+=1
            fp+=1
        
        while rp<len(right_arr):
            pairs[fp] = right_arr[rp]
            rp+=1
            fp+=1
        
        return pairs

