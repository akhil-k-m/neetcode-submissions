class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash1 = {}    

        for word in strs:
            std_word = "".join(sorted(list(word)))
            k = hash1.get(std_word, [])
            k.append(word)
            hash1[std_word] = k
        
        anagrams_list = list(hash1.values())
        return anagrams_list