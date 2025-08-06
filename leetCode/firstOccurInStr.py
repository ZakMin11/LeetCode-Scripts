'''
Zak mineiko
leetcode 28. Find the Index of the First Occurrence in a String
Easy
Completed on Jul 30, 2025
run time: 1 ms (beats 100%)
memory: 17.96 MB (beats 10.54%)
'''

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))

