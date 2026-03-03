import sys
 
input = sys.stdin.readline
 
def read_int():
    return int(input())
 
def invr():
    return list((map(int,input().split())))
 
def insr():
    s = input()
 
    return (list(s[:len(s) - 1]))
 
t = read_int()

for _ in range(t):
    x = read_int()

    a = invr()
    
    #l, r, d, u = a
    
    #if (l == r and l == u and l == d):
    #    print("YES")
    
    #else:
    print("NO")
    