fix = [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29]
fixp = [28, 28, 28, 28, 28, 29, 28, 28, 28, 28, 28, 28, 29]
klasp = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
klas =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = [str(x) for x in input().split(".")]
day = int(n[0])
month = int(n[1])
prestup = n[2]
ct = 0

if prestup == "p":
    ct = sum(klasp[0:month - 1]) + day
else:
    ct = sum(klas[0:month - 1]) + day
print(ct)

month = 1
day = 0
x = 0
if prestup == "p":
    for x in fixp:
        print(x)

        if x >= ct:
            day = ct
            break
        else:

            ct -= x
            month += 1

else:
    for x in fix:
        print(x,"   ",ct)
        if x >= ct:
            day = x
            break
        else:
            ct -= x
            month += 1
print(f"{day}.{month}.{prestup}")
