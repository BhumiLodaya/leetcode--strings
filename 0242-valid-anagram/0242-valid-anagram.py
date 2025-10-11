from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        
        s_counts=Counter(s)
        t_counts=Counter(t)

        return s_counts==t_counts