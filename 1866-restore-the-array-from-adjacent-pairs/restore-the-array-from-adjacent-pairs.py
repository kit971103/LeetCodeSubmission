class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mem = dict()
        seen = set()


        for a, b in adjacentPairs:
            if a in seen: seen.remove(a)
            else: seen.add(a)
            if b in seen: seen.remove(b)
            else: seen.add(b)

            if a in mem: mem[a].append(b)
            else: mem[a] = [b]
            if b in mem: mem[b].append(a)
            else: mem[b] = [a]

        x = seen.pop()
        res = [x, *mem[x]]

        for _ in range(len(adjacentPairs)-1):
            index = res[-1]
            used = res[-2]
            # if mem[end][0] != end: res.append(mem[end][0])
            # else: res.append(mem[end][1])
            for x in mem[index]:
                if x != used: res.append(x)
        return res
            
