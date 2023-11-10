class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        print(f"init: {sx=}, {sy=}")
        print(f"\t{tx=}, {ty=}")

        while ty >= sy and tx >= sx:
            if tx == sx:
                return (ty - sy)%sx == 0
            elif ty == sy:
                return (tx - sx)%sy == 0
            elif ty > tx: ty %= tx
            else: tx %= ty
            print(f"\t{tx=}, {ty=}")
        
        return ty == sy and tx == sx