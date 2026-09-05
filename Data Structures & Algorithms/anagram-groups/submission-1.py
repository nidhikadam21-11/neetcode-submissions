class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for i in strs:
            sortedS = ''.join(sorted(i))
            dict[sortedS].append(i)
        return list(dict.values())