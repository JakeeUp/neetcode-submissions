from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #counting everything automaticcally 

        counts = Counter(nums)


        #get the top k pairs and extract just the numbers using the loop 

        result = []

        for num, freq in counts.most_common(k):
            result.append(num)

        return result
        