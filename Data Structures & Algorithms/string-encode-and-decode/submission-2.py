class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        sizes = []
        for s in strs:
            sizes.append(len(s))
        for size in sizes:
            res += str(size) + ','
        res += '#'
        for s in strs:
            res += s
        return res 


    def decode(self, s: str) -> List[str]:
        # Edge case; empty string, encoding would have done no processing since every loop
        # terminates immediately.
        if s == "": return []
        sizes = []
        res = []
        i = 0
        # Read string sizes until we see the header end character; '#'
        while s[i] != '#':
            parsed_num = ""
            # read number (read digits until ',')
            while s[i] != ',':
                parsed_num += s[i]
                i += 1
            sizes.append(int(parsed_num))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz # move index to next string/word
        return res

