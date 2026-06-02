class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Feels like you'd want to solve the subproblem of: 
        # 'are these two strings anagrams?'. Then solve combinatorially afterwards.
        # Also, two strings of different lengths can't be anagram so that's a simple
        # criteria for rejection that saves time.
        # If you have 3 strings and 1:2 are anagrams and 1:3 are anagrams,
        # then 2:3 are also anagrams, so you only need to compare to the first string.
        # by induction you can do the same for 1:2, 1:3, ..., 1:N as well.
        ''' How did I solve the first one again? you have two strings and
        then you check if they are the same length (1st rejection criteria)
        then you put each character in a hash; character:count, then you compare dicts.
        I will make a list of dicts; a dict for each string, and a key will say how long
        the string is for comparison.

        Turns out my intuitions were wrong!

        The solution is to create a canonical anagram that's used as a key. the canonical anagram is
        a tuple of the frequence of all letters of the alphabet.

        If two strings have the same canonical form then they are anagrams.

        if they're anagrams add them to the list of all items with the same canonical form.
        '''

        groups = {}
        for s in strs:
            # Create the key for for the anagram
            key = [0] * 26
            for c in s:                
                key[ord(c) - ord('a')] += 1
            
            groups.setdefault(tuple(key), []).append(s)
        
        return list(groups.values())

