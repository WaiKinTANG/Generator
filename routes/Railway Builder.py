def rqilwaybuilder(inp):
    oup = []
    for i in inp:
        count = 0
        ls = [int(j) for j in i.split(", ")]
        p = ls[2:]
        p.sort()
        m = [(ls[0] // j) for j in p]
        ind = [0 for j in range(ls[1])]
        while ind[0] <= m[0]:
            r = ls[0]
            for j in range(len(ind)):
                r -= ind[j] * p[j]
            if r == 0:
                count += 1
            ind[-1] += 1
            for j in range(1, len(ind)):
                if ind[-j] > m[-j]:
                    ind[-j] = 0
                    ind[-j-1] += 1
                        
        oup.append(count)
    return oup