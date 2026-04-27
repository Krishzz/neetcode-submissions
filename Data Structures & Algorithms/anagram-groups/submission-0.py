class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        hashmap = {}
        for st in strs:
            sts = "".join(sorted(list(st)))
            if sts in hashmap:
                hashmap[sts].append(st)
            else:
                hashmap[sts] = [st]
        return sorted(list(hashmap.values()))

