ll=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,6,23,27,1,27,5,31,2,9,31,35,1,5,35,39,2,6,39,43,2,6,43,47,1,5,47,51,2,9,51,55,1,5,55,59,1,10,59,63,1,63,6,67,1,9,67,71,1,71,6,75,1,75,13,79,2,79,13,83,2,9,83,87,1,87,5,91,1,9,91,95,2,10,95,99,1,5,99,103,1,103,9,107,1,13,107,111,2,111,10,115,1,115,5,119,2,13,119,123,1,9,123,127,1,5,127,131,2,131,6,135,1,135,5,139,1,139,6,143,1,143,6,147,1,2,147,151,1,151,5,0,99,2,14,0,0]
# 1st solution - 4484226
# ---------------
instruction = 0
input1 = 1
input2 = 2
output = 3

ll[1] = 12
ll[2] = 2
for _ in range(len(ll)):
    if ll[instruction] == 1:
        ll[ll[instruction + output]] = ll[ll[instruction + input1]] + ll[ll[instruction + input2]]
    elif ll[instruction] == 2:
        ll[ll[instruction + output]] = ll[ll[instruction + input1]] * ll[ll[instruction + input2]]
    elif ll[instruction] == 99:
        break
    instruction += 4
print(ll[0])
# 2nd solution - 5696
# ---------------
for noun in range(100):
    for verb in range(100):
        kk = [x for x in ll]
        kk[1] = noun
        kk[2] = verb
        instruction = 0
        input1 = 1
        input2 = 2
        output = 3
        for _ in range(len(ll)):
            if kk[instruction] == 1:
                kk[kk[instruction + output]] = kk[kk[instruction + input1]] + kk[kk[instruction + input2]]
            elif kk[instruction] == 2:
                kk[kk[instruction + output]] = kk[kk[instruction + input1]] * kk[kk[instruction + input2]]
            elif kk[instruction] == 99:
                break
            instruction += 4
            if kk[0] == 19690720:
                print(100 * noun + verb)