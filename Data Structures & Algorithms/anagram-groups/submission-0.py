from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))
            freq_dict[sorted_string].append(string)

        return list(freq_dict.values())