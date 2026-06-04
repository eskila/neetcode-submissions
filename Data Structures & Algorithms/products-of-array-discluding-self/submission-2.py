class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        # How to store repeated work?
        # We can store the multiplication of all elements, and then divide out the value of nums[i]
        # Actually, compute the product of all values, except for values that are 0
        # (because such elements are information destroying)
        count_zero = nums.count(0)

        # All elements will be zero since there will always be multiplication involving
        # at least one zero
        if count_zero > 1: return output  
        
        product = 1
        for num in nums:
            if(num != 0): product *= num
        # print(product)
        
        for i in range(0, len(nums)):
            if count_zero == 1:
                if nums[i] == 0:
                    output[i] = product
                else:
                    output[i] = 0
            else:
                # Scenario with no zeroes
                output[i] = product // nums[i]
        return output