class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set(rooms[0])
        rooms[0] = None
        while keys:
            next_keys = set()
            for key in keys:
                if rooms[key] is not None:
                    next_keys.update(rooms[key])
                    rooms[key] = None
            keys = next_keys
        return  all(map(lambda x: x is None, rooms))

        