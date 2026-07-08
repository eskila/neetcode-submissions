class Solution:
    def trap(self, height: List[int]) -> int:
        # Two-pointer solution
        # The solution will involve moving the pointers l, r given some
        # comparison condition.
        # We need to figure out how much water there is at each height[i]
        # and sum it up in the water variable
        '''
        The lower bar in the l/r pair will set the highest possible
        water level. When pointers meet the summation is finished.
        
        Enumerating the cases/pseudocode
        height[l] < height[r]:
            if height[l] < max_l there must be water there equal to
            max_l - height[l]. water += max_l - height[l]

            If height[l] >= max_l then there is no water there and we also
            set max_l = height[l]

            Finally increment l: l += 1
        
        height[l] > height[r]
            This is the inverse of the previous case:
            if height[r] < max_r there must be water there equal to
            max_r - height[r]. We add it to the sum water: water += max_r - height[r]

            If height[r] >= max_r then there is no water there and we also
            set max_r = height[r]

            Finally we decrement r: r -= 1
        '''
        l, r = 0, len(height) - 1
        water = 0
        max_l = 0 # Max height left
        max_r = 0 # ... right
        while l < r:
            hl = height[l]
            hr = height[r]
            if hl < hr:
                # Case where bar is lower than max_l: There is water
                if hl < max_l:
                    water += max_l - hl
                # Case where bar is taller or equal
                else:
                    max_l = hl
                l += 1
            # The symmetrical case for the right bar
            else:
                if hr < max_r:
                    water += max_r - hr
                else:
                    max_r = hr
                r -= 1
        return water
            


