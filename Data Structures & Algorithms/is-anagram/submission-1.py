class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        s_map = {}
        t_map = {}


        for i,j in zip(s,t):
           s_map[i] =  s_map.get(i,0) + 1
           t_map[j] =  t_map.get(j,0) + 1

        print(s_map, t_map)



        return s_map == t_map