class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        map_s_t ={}
        map_t_s={}

        for ch1 , ch2 in zip (s,t):
            if ch1 in map_s_t:
                if ch1 in map_s_t:
                    if map_s_t[ch1]!=ch2:
                        return False
            elif ch2 in map_t_s:
                return False
            else:
                map_s_t[ch1]=ch2
                map_t_s[ch2]=ch1
        return True



        