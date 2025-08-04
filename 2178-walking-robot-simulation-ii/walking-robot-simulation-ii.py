# NOTE: its after checking other solution, and rewrite with my own logic and commnet
class Robot:

    def __init__(self, width: int, height: int):
        # as the robot must follow a cirle path, so it state can be repersent by a path with an index
        # list[(x, y, direction)]
        self.path: list[tuple[int, int, str]] = []
        self.path.extend((x, 0, "East") for x in range(width)) # <--- [0,0,"East"]
        self.path.extend((width - 1, y, "North") for y in range(1, height))
        self.path.extend((x, height - 1, "West") for x in range(width - 2, -1, -1))
        self.path.extend((0, y, "South") for y in range(height - 2, 0, -1))

        self.path_length = len(self.path)
        self.steps = 0
        self.index = 0

    def step(self, num: int) -> None:
        self.steps += num
        self.index = self.steps % self.path_length

    def getPos(self) -> List[int]:
        return self.path[self.index][0:2]

    def getDir(self) -> str:
        if self.index == 0 and self.steps != 0:
            # special case for initial direction, if moved(steps != 0) and index == 0, should be South
            return "South"
        return self.path[self.index][2]



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()