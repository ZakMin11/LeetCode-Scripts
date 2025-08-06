'''Zak mineiko
leetcode 43. Multiply Strings
Medium
complete
run time: 0ms (beat 100%)
memory: 17.64 MB (beats 89.67%)
'''

'''
strat:
    use python's int() to convert string to int
    return the two ints multiplied by eachother
'''

def multiply(num1, num2):
    return str(int(num1) * int(num2))
