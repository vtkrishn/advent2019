def check1(kk):
    length = len(kk)
    for i in range(length-1):
        if kk[i] == kk[i+1]:
            continue
        if kk[i] > kk[i+1]:
            return True
    return False
def check2(kk):
    length = len(kk)
    a_flag = False
    b_flag = False
    for i in range(length-1):
        if (i == 0 or kk[i] != kk[i-1]) and kk[i] == kk[i+1] and (i == length-2 or kk[i] != kk[i+2]):
            a_flag = True

    for i in range(length - 1):
        if kk[i] > kk[i+1]:
            b_flag = True

    return a_flag and not b_flag


ans1 = 0
ans2 = 0

total = 0
for x in range(387638, 919123):
    if check1(str(x)):
        ans1 += 1

    if check2(str(x)):
        ans2 += 1

    total += 1

# 1st solution - 466
# ---------------
print(total-ans1-1)
# 2nd solution - 292
# ---------------
print(ans2)