class Solution:
    def countTime(self, time: str) -> int:

        if time[0] == "?" and time[1] == "?": hh = 24
        elif time[0] == "?":
            if 0 <= int(time[1]) <= 3: hh = 3
            else: hh = 2
        elif time[1] == "?":
            if time[0] == "2": hh=  4
            else: hh = 10
        else: hh = 1

        if time[3] == "?" and time[4] == "?": mm = 60
        elif time[3] == "?": mm = 6
        elif time[4] == "?": mm = 10
        else: mm = 1

        return hh*mm
        
        


        