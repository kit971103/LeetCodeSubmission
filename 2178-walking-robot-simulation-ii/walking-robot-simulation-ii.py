class Robot:

    def __init__(self, width: int, height: int):
        self.direction: str = "East"
        self.x, self.y = 0, 0
        self.w, self.h = width - 1, height - 1
        self.cycle_size = 2 * (self.w + self.h)  # step takes for one cycle
        assert self.cycle_size > 0
        # print(f"Init: {self.w, self.h}")

    def step(self, num: int) -> None:
        # print(f"Step: {num}")
        # remove the cycle move
        num %= self.cycle_size
        # handle special facing:
        if any(
            [
                self.direction == "North" and (self.x, self.y) == (self.w, 0),
                self.direction == "East" and (self.x, self.y) == (0, 0),
                self.direction == "South" and (self.x, self.y) == (0, self.h),
                self.direction == "West" and (self.x, self.y) == (self.w, self.h),
            ]
        ):
            self._turn()
            self._turn()
            self._turn()

        # walk along the wall
        while num > 0:
            # print(f"\tpos={self.x, self.y}, dir={self.direction}")
            if self._facing_wall():
                self._turn()
            walked = self._walk(num)
            num -= walked
        # print(f"\t-->Stop at {self.x, self.y} @{self.direction}")

    def getPos(self) -> List[int]:
        # print(f"getPos: {self.x, self.y}")
        return [self.x, self.y]

    def getDir(self) -> str:
        # print(f"getDir: {self.direction}")
        return self.direction

    # ------------------- intyernal helper ------------------------------
    def _facing_wall(self) -> bool:
        # NOTE: use >= for unexpted out of bound
        return any(
            [
                self.direction == "North" and self.y >= self.h,
                self.direction == "East" and self.x >= self.w,
                self.direction == "South" and self.y <= 0,
                self.direction == "West" and self.x <= 0,
            ]
        )

    def _walk(self, step: int) -> int:
        if self.direction == "East":
            walked = min(step, self.w - self.x)
            self.x += walked
        elif self.direction == "North":
            walked = min(step, self.h - self.y)
            self.y += walked
        elif self.direction == "West":
            walked = min(step, self.x)
            self.x -= walked
        else:
            walked = min(step, self.y)
            self.y -= walked
        return walked

    def _turn(self) -> None:
        if self.direction == "East":
            self.direction = "North"
        elif self.direction == "North":
            self.direction = "West"
        elif self.direction == "West":
            self.direction = "South"
        else:
            self.direction = "East"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
