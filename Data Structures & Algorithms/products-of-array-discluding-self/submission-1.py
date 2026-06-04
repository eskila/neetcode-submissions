class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        # How to store repeated work?
        # We can store the multiplication of all elements, and then divide out the value of nums[i]
        # Actually, compute the product of all values, except for values that are 0
        # (because such elements are information destroying)
        product = 1
        for num in nums:
            if(num != 0): product *= num
        print(product)
        
        for i in range(0, len(nums)):
            print(i)
            sub_array = nums[:i] + nums[i+1:]
            if 0 in sub_array:
                output[i] = 0
            elif(nums[i] == 0):
                output[i] = product
            else:
                output[i] = int(product / nums[i])
        return output