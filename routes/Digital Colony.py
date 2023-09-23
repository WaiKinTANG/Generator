def main(gen, col): #gen as number, col as string
    num = [int(col[i]) for i in range(len(col))]
    for g in range(gen):
        w = sum(num) % 10
        newnum = [((w + 10 + num[i] - num[i + 1]) % 10) for i in range(len(num) - 1)]
        nextgen = []
        for i in range(len(newnum)):
            nextgen.append(num[i])
            nextgen.append(newnum[i])
        nextgen.append(num[-1])
        num = nextgen.copy()
    return sum(num)

print(main(10, "1000"))
print(main(50, "1000"))