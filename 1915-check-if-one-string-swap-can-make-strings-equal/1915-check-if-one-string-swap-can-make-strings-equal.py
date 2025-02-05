class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        v=set()
        f=set()
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                c+=1
                v.add(s1[i])
                f.add(s2[i])
        return (c==2 and len(v)==2 and v==f) or c==0