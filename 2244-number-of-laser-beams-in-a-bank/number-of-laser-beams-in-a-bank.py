class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        a=[]
        for i in bank:
            c = i.count('1')
            if c!=0:
                a.append(c)
        for j in range (len(a)-1):
            ans+=(a[j]*a[j+1])
        return (ans)