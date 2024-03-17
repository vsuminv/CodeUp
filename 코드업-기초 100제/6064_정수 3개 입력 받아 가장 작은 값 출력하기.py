a, b , c = map(int, input().split())


print( (b if a>b else a) if ((a if a<b else b)<c) else c)

