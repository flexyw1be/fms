# a = ''.join(input().split()) + '1'
# print(a.split('0'))
a = input().split()
a.append("1")

cnt = 0
for i in range(1, len(a)):
    if(a[i-1] == '0' and a[i] != '0'):
        cnt += 1
print(cnt)