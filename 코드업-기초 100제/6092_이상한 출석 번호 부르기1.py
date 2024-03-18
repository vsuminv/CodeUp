n = int(input())
chk = input().split()

cnt_list = [0]*24
for i in range(n):
    chk[i] = int(chk[i])
    cnt_list[chk[i]] += 1

for i in range(1, 24):
    print(cnt_list[i], end = ' ')
