class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        delta = (sumB - sumA) // 2  # This is the value Bob's candy - Alice's candy
        
        setB = set(bobSizes)  # Convert to set for fast lookup
        
        for x in aliceSizes:
            if x + delta in setB:
                return [x, x + delta]
        