class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr)-1: return max(arr)
        winner = arr[0]
        win_count = 0
        for n in arr[1:]:
            if winner > n: 
                win_count+=1
            else:
                winner = n
                win_count =1
            if win_count == k: break
        return winner
        