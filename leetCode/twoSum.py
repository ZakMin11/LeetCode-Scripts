# Zak Mineiko
# leet code 15. 3Sum
# Medium

# runtime: 1652 ms beats 29%
# memory: 17.33 MB beats 72%
# done
def findTarget(l, target):
	for i in range(len(l)):
		for x in range(i+1, len(l)):
			print(i,x)
			print(l[i],l[x], "=", l[i]+l[x])
			if l[i]+l[x] == target:
				return [i,x]

# second go, O(n*n) not acceptable smh
def findTarget2(l, target):
	for i,c in range(l):
		if 
		#c+=1
		c=i+3

l = [2,7,11,15]
#l = [3,3]
target = 26
print(findTarget(l, target))
		
