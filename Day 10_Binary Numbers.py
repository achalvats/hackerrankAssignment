# def count_ones(ones):
#     count = 1
#     li = []
#     for i in range(len(ones)):
#         try:
#             #print("true 0"+str(ones[i]))
#             #print(ones[i])
#             if ones[i] == '1':
#                 #print("true 11")
#                 if ones[i + 1] == '1':
#                     count += 1
#                 else:
#                     li.append(count)
#                     count = 1
#         except IndexError:
#             li.append(count)
#     return li


if __name__ == "__main__":
    # binary = bin(int(input()))[2:]
    # print(max(count_ones(binary)))

    print(len(max(bin(int(input().strip()))[2:].split('0'))))