prices = [25000, 30000, 45000, 50000, 55000, 60000]

target = 50000

low = 0
high = len(prices) - 1
ans = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

if ans != -1:
    print("First Product Price:", prices[ans])
    print("Index:", ans)
else:
    print("No Product Found")
