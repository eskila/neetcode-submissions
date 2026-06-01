class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        # Easy mode!
        #return Counter(s) == Counter(t)

        s_dict = {}
        t_dict = {}

        # This dictionary method looks for the character.
        # If it doesn't exist yet, it safely returns 0 instead of 
        # throwing a KeyError
        for c in s:
            s_dict[c] = s_dict.get(c,0) + 1

        for c in t:
            t_dict[c] = t_dict.get(c,0) + 1

        return s_dict == t_dict