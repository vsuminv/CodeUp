
arr = []
         
for i in range(10):
     arr.append(list(map(int, input().split())))

x, y = 1,1 #배열은 0부터 시작하기 떄문에 2,2 자리는 1,1로 설정

while True:
     if arr[x][y] == 0:
          arr[x][y] = 9
     elif arr[x][y] == 2:
          arr[x][y] = 9
          break

     if ((arr[x][y+1] == 1 and arr[x+1][y] == 1)): #양쪽이 1일 경우
        break

     if (arr[x][y+1] != 1): #벽이 아닐 시 오른쪽으로 한 칸 이동
        y = y + 1
     elif (arr[x+1][y] != 1): #오른쪽에 벽이 있고, 벽이 아래쪽에 없으면 아래로 이동
        x = x + 1
print()
     
for i in range(10):
    for j in range(10):
         print(arr[i][j],end = ' ')
    print(' ')
 

