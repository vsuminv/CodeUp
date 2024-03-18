h, w = map(int,input().split())

n = int(input())
arr = []

for i in range(h):
    arr.append([])
    for j in range(w):
        arr[i].append(0)


for i in range(n):
    l,d,x,y = map(int,input().split())

    for j in range(l):
        if d == 0:
            arr[x-1][y-1+j] = 1
        else:
            arr[x-1+j][y-1] = 1
for i in range(h):
    for j in range(w):
        print(arr[i][j], end = ' ')
    print('\n')





