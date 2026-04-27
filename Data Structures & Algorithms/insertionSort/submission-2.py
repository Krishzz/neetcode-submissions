# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        steps = []
        n = len(pairs)

        for i in range(n):
            key = pairs[i]
            j = i - 1

            # Shift larger elements to the right
            while j >= 0 and pairs[j].key > key.key:
                pairs[j + 1] = pairs[j]
                j -= 1

            # Insert the key back
            pairs[j + 1] = key

            # Capture snapshot after this pass
            steps.append(pairs[:])

        return steps