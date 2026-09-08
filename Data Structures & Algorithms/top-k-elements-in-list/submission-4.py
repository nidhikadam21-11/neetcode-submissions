class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        freq=[[] for i in range(len(nums)+1)]
        for i in nums:
            dict1[i] = 1 + dict1.get(i,0)
        for n,cnt in dict1.items():
            freq[cnt].append(n)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res