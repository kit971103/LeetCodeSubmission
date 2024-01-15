class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        seen = set()
        for winner, loser in matches:
            if winner not in seen:
                seen.add(winner)
                zero_loss.add(winner)
            
            if loser not in seen:
                seen.add(loser)
                one_loss.add(loser)
            elif loser in zero_loss:
                zero_loss.discard(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.discard(loser)
        
        return [sorted(list(zero_loss)), sorted(list(one_loss))]


        