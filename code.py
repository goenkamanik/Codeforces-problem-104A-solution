n = int(input())
temp = 10
ans = 0
if(n > temp and n <= 21):
    if(n - temp == 10):
        ans = 15
    else:
        ans = 4

print(ans)