n = int(input())

arr = []

for i in range(20):
    arr.append([]) #새로운 배부 배열 선언
    for j in range(20):
        arr[i].append(0) #해당 내부에 0이라는 값 추가


for i in range(n):
    x, y = map(int, input().split())
    arr[x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(arr[i][j], end = ' ')
    print('\n')
