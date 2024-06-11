from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs:
            l = len(s)
            output += str(l) + '#' + s
        print(output)
        return output
    def decode(self, s: str) -> List[str]:
        i, res = 0, []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            start = j+1
            end = start + l
            sl = s[start:end]
            res.append(sl)
            i = end
        return res
print(Solution().decode(Solution().encode(["neet","code","love","youiiiiiiiiiii"])))




#
# class Solution:
#     def encode(self, strs: List[str]) -> str:
#         if not len(strs):
#             print("empty")
#             return None
#         output = ''
#         for words in strs:
#             output += words
#             output += chr(5000)
#
#         print('output', output)
#         return output
#     def decode(self, s: str) -> List[str]:
#         if not s:
#             return []
#         s = s[: len(s) - 1]
#         res = s.split(chr(5000))
#         print(res)
#         return res
#
# print(Solution().decode(Solution().encode([""])))