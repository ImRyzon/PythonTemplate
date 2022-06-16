import sys
import collections
import bisect
import math
# sys.setrecursionlimit(100000)          <---- ONLY UNCOMMENT IF YOU ARE EXPERIENCING MEMORY LIMIT ISSUES
readLine = lambda: sys.stdin.readline().strip()
readInt = lambda: int(sys.stdin.readline())
printf = lambda x: sys.stdout.write(f"{x}\n")
prints = lambda x: sys.stdout.write(x)
printine = lambda x: list(map(printf, x))
printeach = lambda x, y="": print(*x, sep=y)
gi = lambda: list(map(int, readLine().split()))
gs = lambda: readLine().strip().split()
emp = lambda x, y: [x] * y
fill = lambda x: list(range(1, x + 1))
flat = lambda x, l: x.join(map(str, l))
max_int, min_int = float('inf'), float('-inf')
######################## End of Template #######################




