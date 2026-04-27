# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
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

