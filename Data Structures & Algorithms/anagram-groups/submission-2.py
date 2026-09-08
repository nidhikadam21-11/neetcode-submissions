class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1= defaultdict(list)
        for i in strs:
            a = ''.join(sorted(i))
            dict1[a].append(i) 
        return list(dict1.values())