"""
Slide a window of length 10 over the DNA string; each window is a candidate substring
Track which substrings we have seen; if we see the same 10-mer again, add it to the result
For speed/memory, we can encode A/C/G/T in 2 bits and use a rolling hash
"""
"""
Time Complexity: O(n)
Space Complexity: O(n) (in worst case storing many 10-mers)
"""


class repeatedDNA:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        L = 10
        if len(s) <= L:
            return []
        seen = set()
        dup = set()
        for i in range(len(s) - L + 1):
            sub = s[i:i+L]
            if sub in seen:
                dup.add(sub)
            else:
                seen.add(sub)
        return list(dup)


if __name__ == "__main__":
    obj = repeatedDNA()
    print(sorted(obj.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")))
    # ["AAAAACCCCC", "CCCCCAAAAA"]

    print(sorted(obj.findRepeatedDnaSequences("AAAAAAAAAAAAA")))
    # ["AAAAAAAAAA"]

