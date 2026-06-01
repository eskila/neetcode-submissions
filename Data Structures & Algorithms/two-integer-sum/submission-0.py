class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            needed = target - num
            # See if needed is in the dict, otherwise keep looking
            idx = num_map.get(needed,-1)
            if idx != -1:
                return [idx, i]
            num_map[num] = i

'''
We need to figure out if we cached the needed number already, and if so get its index so
we can return it.

idx will always be less than i because it was always seen prior to the current iteration.
'''
                