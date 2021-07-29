def coordinates(x, y, z, n):
    corr = []
    # sub_corr = [x,y,z]
    for i in range(x + 1):
        # sub_corr[0] = i
        for j in range(y + 1):
            # sub_corr[1] = j
            for k in range(z + 1):
                # sub_corr[2] = k
                # print(sub_corr)
                if i + j + k != n:
                    corr.append([i, j, k])
                # print(corr)

    print(corr)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n])
    # coordinates(x, y, z, n)
