# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res=[]
        if not pairs:
            return res
        for i in range(len(pairs)):
            j=i-1
            c=pairs[i]
            while (j>=0 and pairs[j].key > c.key):
                pairs[j+1]=pairs[j]
                j-=1

            pairs[j+1]=c
            res.append(pairs[:])
        return res
        