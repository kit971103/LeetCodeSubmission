class Solution:
    def generate(self, numRows):
        pas=[[] for i in range(numRows)]

        for i in range(numRows):
            pas[i]=[[] for j in range(i+1)]
            for j in range(i+1):
                if j==0 or j==i:
                    pas[i][j]=1
                else: 
                    pas[i][j]=pas[i-1][j-1]+pas[i-1][j]
        return pas