class Solution:
    def smallestSubarrays(self, a: List[int]) -> List[int]:
        # max imput = 10^9 < 2^30, so 32 bit will be enough
        bit_map = [[] for _ in range(32)]

        # bulid the bit map
        for index in range(len(a)-1, -1, -1):
            n = a[index]
            offset = 0
            while n > 0:
                if n%2:
                    bit_map[offset].append(index)
                n = n >> 1
                offset+=1
        # print(bit_map)
        
        answer = []
        for index in range(len(a)):
            is_one = []
            for indexes in bit_map:
                if not indexes:
                    continue
                if indexes[-1] < index:
                    indexes.pop()
                if indexes:
                    is_one.append(indexes[-1])
            # print(f"{index=}, {is_one=}")
            answer.append(max(is_one) - index + 1 if is_one else 1)
        
        return answer

    
                
