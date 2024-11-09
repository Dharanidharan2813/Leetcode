class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[]
        for i in range(rowIndex+1):
            r=[]
            for j in range(i+1):
                res=comb(i,j)
                r.append(res)
            a.append(r)
        return a[-1]