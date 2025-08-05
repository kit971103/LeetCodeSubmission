class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        compress_len = 0
        repeat = chars[0]

        for i, c in enumerate(chars):
            if c == repeat:
                count += 1
            else:
                # write the letter
                chars[compress_len] = repeat
                compress_len += 1

                if count > 1:
                    count_str = str(count)
                    chars[compress_len : compress_len + len(count_str)] = count_str
                    compress_len += len(count_str)
                # reset counting
                start = i
                repeat = c
                count = 1
        else:
            # write the letter
            chars[compress_len] = repeat
            compress_len += 1
            if count > 1:
                count_str = str(count)
                chars[compress_len : compress_len + len(count_str)] = count_str
                compress_len += len(count_str)


        return compress_len
