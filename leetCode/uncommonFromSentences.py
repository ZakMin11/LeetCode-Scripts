'''
Zak Mineiko
Leetcode 884. Uncommon Words from Two Sentences
easy
incomplete
runtime: 
memory:
'''
# remove all repeats
# combine both lists, turn to dict, return dict as list

class Solution:
    def uncommonFromSentences(self, s1, s2): 
        uncommon = []
        l1 = s1.split(" ")
        l2 = s2.split(" ")
        full = l1 + l2
        print(full)
        if True:
            return list(set(full))
        for i in range(len(full)):
            temp = full[i]
            full[i]=""
            if temp in full:
                full[temp]=""
            else:
                uncommon.append(temp)


        return uncommon

    def tryThis(self, s1,s2):
        common = []
        s1 = s1.split()
        s2 = s2.split()
        l1 = (list(set(s1)))
        l2 = (list(set(s2)))
        l1.sort(key=len)
        l2.sort(key=len)
        print(l1,l2)
        if len(l1) <= len(l2):
            for i in l1:
                if i in l2 and i not in common:
                    print(i, l1,l2)
                    l1.remove(i)
                    l2.remove(i)
                    
        return list(set(l1+l2))
#        for i in range(max(len()))
#        return list(dict(s1+s2))
    
    #def uncommonFromSentences(self, s1, s2):
    #    l1 = s1.split()
    #    l2 = s2.split()
    #    uncommon = []
    #    for i in range(len(max(l1,l2))):
    #        if l1[i] not in l2:
    #            uncommon.append(l1[i])
    #    for i in range(len(min(l1,l2))):
    #        if l2[i] not in l1:
    #            uncommon.append(l2[i])
    #    #print(print(uncommon))
    #    # return uncommon 

    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    
    print(tryThis(0, s1,s2))
    #s1 = "apple apple"
    #s2 = "banana"
#    print(uncommonFromSentences(0, s1, s2))
