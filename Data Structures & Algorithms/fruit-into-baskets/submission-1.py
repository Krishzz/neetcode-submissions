class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        max_fruits = 0
        l = 0
        for r in range(len(fruits)):
            fruit_type = fruits[r]
            basket[fruit_type] = basket.get(fruit_type, 0)+1
            while len(basket)>2:
                fruit_left = fruits[l]
                basket[fruit_left] -=1
                if basket[fruit_left] == 0:
                    del basket[fruit_left]
                l+=1
            max_fruits = max(max_fruits, r-l+1)
        return max_fruits