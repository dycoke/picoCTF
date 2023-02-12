base = int(input())
nums = input().split(' ')

ans = ""
for num in nums:
    ans += chr(int(num, base))

print(ans)
