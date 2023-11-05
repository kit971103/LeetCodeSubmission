class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if  k == 1: return max(arr[0], arr[1])
        
        winner = arr[0]
        win_count = 0
        for n in arr[1:]:
            if winner > n: 
                win_count+=1
                if win_count == k: break
            else:
                winner = n
                win_count =1
        return winner
        