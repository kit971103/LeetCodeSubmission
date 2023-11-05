class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k >= len(arr)-1: return max(arr)
        if  k == 1: return max(arr[0], arr[1])
        
        winner = arr[0]
        win_count = 0
        for i in range(1, len(arr)):
            if winner > arr[i]: 
                win_count+=1
                if win_count == k: break
            else:
                winner = arr[i]
                win_count = 1
        return winner
        