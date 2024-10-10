class Solution:
    def minOperations(self, logs):
        spot = 0
        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif logs[i] == "../":
                spot -=1
            else:
                spot+=1
            if spot<0:
                spot = 0
        return spot
    #l = ["d1/","d2/","../","d21/","./"]
    #l=["d1/","d2/","./","d3/","../","d31/"]
    l=["d1/","../","../","../"]
    print(minOperations(0,l))
