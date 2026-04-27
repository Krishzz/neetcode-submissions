class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        max_fruits = 0
        l = 0
        for r in range(len(fruits)):
            fruit_type = fruits[r]
            baskets[fruit_type] = baskets.get(fruit_type, 0) + 1
            while len(baskets) > 2:
                left_fruit = fruits[l]
                baskets[left_fruit] -= 1
                if baskets[left_fruit] == 0:
                    del baskets[left_fruit]
                l+=1
            max_fruits = max(max_fruits, r-l+1)
        return max_fruits