slovo = input()
numerals = [str(x) for x in range(0, 10)]


def zisti_int(slk, a):
    ct = 0
    for x in range(a, len(slk)):
        if slk[x] in numerals:
            ct += 1
        else:
            return int(slk[a:a + ct]), ct  # number and number of digits that this number has


def medzi_zatvorky(slk, a):
    ct = 0
    start, end = 0, 0
    for x in range(a, len(slk)):
        if slk[x] == "(":
            if ct == 0:
                start = x
            ct += 1

        elif slk[x] == ")":
            ct -= 1
            if ct == 0:
                end = x
                break

    return start + 1, 0 + end


def solve(slovo):
    for x in range(len(slovo)):
        if slovo[x] in numerals:
            a, b = zisti_int(slovo, x)

            if slovo[x + b] == "(":
                z, y = medzi_zatvorky(slovo, x + b)
                lst = [slovo[0:x], str(a * slovo[z:y]), slovo[y + 1:len(slovo)]]

                return solve("".join(lst))

            else:
                lst = [slovo[0:x], a * slovo[x + b], slovo[x + b + 1:len(slovo)]]

                return solve("".join(lst))
        elif x == len(slovo) - 1:
            print(slovo)
            break


solve(slovo)