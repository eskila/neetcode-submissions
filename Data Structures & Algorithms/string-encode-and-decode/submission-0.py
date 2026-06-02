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
        if s == "": return []
        sizes = []
        res = []
        i = 0
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
            i += sz
        return res

