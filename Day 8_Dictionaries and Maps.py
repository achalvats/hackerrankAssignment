if __name__ == '__main__':
    li = []
    dic = {}
    for _ in range(int(input())):
        li.append(str(input()))
    for i in range(len(li)):
        x = li[i].split()
        dic[x[0]] = x[1]

    while True:
        try:
            name = input()
            if name in dic:
                print('%s=%s' % (name, dic[name]))
            else:
                print('Not found')
        except:
            break
# n = int(input())
# name_numbers = [input().split() for _ in range(n)]
# phone_book = {k: v for k,v in name_numbers}
# while True:
#     try:
#         name = input()
#         if name in phone_book:
#             print('%s=%s' % (name, phone_book[name]))
#         else:
#             print('Not found')
#     except:
#         break