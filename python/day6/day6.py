from collections import deque, defaultdict
A= defaultdict(list)
B= defaultdict(list)
for line in open('3.in').readlines():
    key1,key2 = line.strip().split(')')
    A[key1].append(key2)
    B[key1].append(key2)
    B[key2].append(key1)

def check(i):
    count = 0
    for j in A.get(i, []):
        count += check(j)
        count += 1
    return count

count = 0
for i in A:
    count += check(i)
# 1st solution - 314247
# ---------------
print(count)

p = {}
q = deque()
q.append(('YOU', 0))

while q:
    x, d = q.popleft()
    if x in p:
        continue
    p[x] = d
    for y in B[x]:
        q.append((y, d+1))
# 2nd solution - 514
# ---------------
print(p['SAN']-2)
