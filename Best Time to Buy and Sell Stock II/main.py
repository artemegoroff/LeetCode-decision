from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def getCounter(word):
            return Counter(word)

        def isAnagram(word1, word2):
            return getCounter(word1) == getCounter(word2)

        anagrams = []
        check_dict = {}
        num_group = 0
        for angrm in strs:
            is_find = False
            angrm_counter = getCounter(angrm)
            for key in check_dict:
                if check_dict[key] == angrm_counter:
                    anagrams[key].append(angrm)
                    is_find = True
                    break
            if not is_find:
                anagrams.append([angrm])
                check_dict[num_group] = angrm_counter
                num_group += 1

        return anagrams


s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

