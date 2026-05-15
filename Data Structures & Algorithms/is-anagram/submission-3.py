class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for st in s:
            hashmap[st]=hashmap.get(st, 0)+1
        for ts in t:
            hashmap[ts]=hashmap.get(ts, 0)-1
        return all(val == 0 for val in hashmap.values())