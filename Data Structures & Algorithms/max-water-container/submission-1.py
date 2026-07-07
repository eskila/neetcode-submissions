class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest_volume = 0
        left, right = 0, len(heights) - 1
        
        while left < right:
            hl = heights[left]
            hr = heights[right]
            vol = (right - left) * min(hl, hr)
            largest_volume = max(vol, largest_volume)
            if hl < hr:
                left += 1
            else:
                right -= 1
        
        return largest_volume