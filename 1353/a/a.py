from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, m = iis()	
	if n > 2:
		print(m*2)
	elif n == 2:
		print(m)
	else:
		print(0)