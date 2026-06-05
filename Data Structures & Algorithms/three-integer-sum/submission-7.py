class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # mutate in place to not add O(N) space
        print(nums)
        l = 0
        n = len(nums) - 1
        # We observe that adding a sorted left and right number, the
        # left number is always smaller than the right, so by adding a 3rd number in between,
        # we can find the one that adds to create a zero-sum.
        # How do we make sure we're not adding any duplicate triplets?
        # A: We just have to move one of the pointers: l+1 until it points to a larger number,
        # and then the sum needs different variable combinations to sum to zero.
        result = []
        while(l < n - 1):
            num_l = nums[l]
            # l + m + r = 0
            # therefore l = -m - r
            m = l + 1
            r = n
            while m < r:
                num_m = nums[m]
                num_r = nums[r]
                if(num_r + num_m + num_l == 0): # Found a solution:
                    result.append([num_l, num_m, num_r])
                    # This pair of m, r should not reappear to avoid duplicates
                    # so move the pointers
                    # Will create a duplicate if both pointer point to the same numbers though
                    m += 1
                    r -= 1
                    
                    # Skip duplicates of m:
                    while(m < r and nums[m] == nums[m-1]):
                        m += 1
                    
                    # Skip duplicates of r:
                    while(m < r and nums[r] == nums[r+1]):
                        r -= 1
                    
                # walk m pointer right to get a larger number
                elif(num_r + num_m + num_l < 0):
                    m += 1
                # Walk r pointer left to get a smaller number
                else:
                    r -= 1

            # keep moving the pointer if there's a duplicate
            while nums[l] == nums[l+1] and l < n - 1:
                l += 1
            
            # But always need to move the pointer regardless
            l += 1

        return result
        