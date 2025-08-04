class Solution(object):
    def compress(self, chars):

        rep= chars[0]
        n= 1
        m= 0

        for i in range(1, len(chars)):
            c = chars[i]
            if c == rep: 
                n += 1
            else:
                chars[m] = rep
                m+=1
                if n > 1:
                    n= str(n)
                    chars[ m: m + len(n) ] = n
                    m += len(n)
                rep=c
                n = 1
            # print(chars)
        else:
            chars[m] = rep
            m+=1
            if n > 1:
                n= str(n)
                chars[ m: m + len(n) ] = n
                m += len(n)
        # print(chars)
        return m
        