class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        chars_count = {}

        for char in s:
            chars_count[char] = chars_count.get(char, 0) + 1
        
        for char in t:
            if char not in chars_count:
                return False
            
            chars_count[char] -= 1
        
        return all(value == 0 for value in chars_count.values())

        