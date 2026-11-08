class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            s_lower = s.lower()
            k = [ 0 ] * 26
            for char in s_lower:
                char_index = ord(char) - ord("a")
                k[char_index] += 1
            group[",".join([str(i) for i in k])].append(s)
        return [v for v in group.values()]

