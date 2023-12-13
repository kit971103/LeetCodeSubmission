class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for row, col in product(range(len(mat)), range(len(mat[0]))):
            # print(f"{row}, {col}")
            # print(mat[row])
            # print([mat[i][col] for i in range(len(mat))])
            if sum(mat[row]) == 1 and sum([mat[i][col] for i in range(len(mat))])==1 and mat[row][col] == 1:
                # print(f"add at {row}, {col}")
                count +=1
        return count

        