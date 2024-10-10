class Solution:
    def reverse(self, x: int) -> int:
        # 32 bit signed integer: 2^32 = 4294967296 values

        # signed int -> bits: 00000000000000000000000000000000-111111111111111111111111
        #   value: -2^32 / 2 <-> (2^32 / 2) - 1
        #   value: -2147483648 <-> 2147483647

        #s = str(x)
        #r = s[::-1]
        if x<0: # if negative
            s = str(x)
            r = s[1:]
            r = r[::-1]
            if abs(int(r)) > 2147483648: # if too big
                return 0
            else:
                return -int(r)
        elif x==0:
            return 0
        else: # if positive
            s = str(x)
            r = s[::-1]
            print(r)
            if abs(int(r)) > 2147483647: # if too big
                return 0
            else:
                return int(r)

    x = 120
    print(reverse(0, x))
    # accepted    
