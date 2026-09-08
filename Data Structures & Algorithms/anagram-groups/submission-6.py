class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=defaultdict(list)
        for i in strs:
            count= [0]*26
            for s in i:
                count[ord(s)-ord('a')]+=1
            dict1[tuple(count)].append(i)
        return list(dict1.values())