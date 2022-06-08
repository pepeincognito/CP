lst = [int(x) for x in input().split()]
nums = 0
for x in range(1, 7):
    if lst.count(x) >= 4:
        print(x * 100 + sum(lst) - 4 * x)

        break
    if x in lst:
        nums += 1
        if nums == 6:
            print(1000)
            break
    if x == 6:
        print(sum(lst))