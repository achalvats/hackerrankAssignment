if __name__ == '__main__':
    li = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name,score])

    for i in range(len(li)):
        print(str(i)+"before"+str(li))

        if li[i+1][1] is not None and li[i][1] > li[i + 1][1]:
            temp = li[i]
            li[i] = li[i+1]
            li[i+1] = temp
            print(str(i)+"after"+str(li))