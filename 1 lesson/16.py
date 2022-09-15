n = int(input())
a = [int(input()) for x in range(n)]
print('Yes' if a == sorted(a) else 'No')
