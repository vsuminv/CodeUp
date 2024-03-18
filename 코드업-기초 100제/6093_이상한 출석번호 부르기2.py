n = int(input())

num = input().split()

for i in range(n):
    num[i] = int(num[i])
    num.reverse()
    print(num[i], end = ' ')