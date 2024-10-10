class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        count = len(s/2)
        #for y in range(numRows):


        #print(s)


s = "PAYPALISHIRING"
numRows = 4


for y in range(len(s)//2):
    for x in range(len(s)//3):
        print(s[y])

print(len(s)//2)
#print(convert(s))
#print(convert(s) == "PAHNAPLSIIGYIR")
