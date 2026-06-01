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

        '''
        When is a problem a hash problem? What's the pattern?

        Comparing two objects, are they the same in some way?

        What is the strategy?
        Scan the array, map the results

        Save occurences of elements in some kind of map so they can be looked up
        later in linear (or constant?) time. Map saves important information I've
        already seen.

        The questionx to ask are:
        1.  What do I need to know instantly while I scan?
            this case: how many times a letter already occured

            In the find duplicates problem: has this number already occured in the
            array?
        2. What would make this (array) element a part of the solution?

        '''