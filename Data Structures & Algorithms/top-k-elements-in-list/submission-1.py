class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sorting algorithm

        # Max frequency is the length of numns, so there has to be an array slot
        # freq[len(nums)], since array indices start at 0, create one more slot.
        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        # Pairing numbers to their frequencies in a hash map. num : count
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # The bucket sorting part:
        # Iterate the map and build the frequency array
        # The count places the number in freq. Two numbers of the same frequency
        # would get appended to the same slot in the array.
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Build the result list (stop when we have added k items)
        result = []
        # step backward from the highest freq to lowest using negative indexing
        for i in range(-1, -len(freq), -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result