import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Right/Left pointer solution
        left, right = 0, len(s) - 1
        while (left < right):
            # Skip non-letters from the left
            while left < right and not s[left].isalnum():
                left += 1
                
            # Skip non-letters from the right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare the characters case-insensitively
            # Note that only 2 characters are created, then GC:d
            if s[left].lower() != s[right].lower():
                return False
                
            # Move pointers closer together
            left += 1
            right -= 1
            
        return True
        # Prep the string by removing non-alphabetic characters and
        # lowercasing it
        # But: doing it like this creates O(N) space complexity
        '''
        s2 = re.sub(r"[^a-zA-Z]", "", s).lower()
        #print(s2)
        n = len(s2)
        #print(n)
        for i in range(n):
            if (s2[i] != s2[n-i-1]): return False

        return True
        '''