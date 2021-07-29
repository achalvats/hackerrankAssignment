# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    count = int(input("enter the count"))
    li = []
    for _ in range(count):
        li.append(str(input("enter the input")))
    li_new = []
    for element in li:
        #print(element)
        str_odd = ''
        str_even = ''
        for i in range(len(element)):
            if i % 2 == 0:
                str_odd += element[i]
                #print(element[i])
            else:
                str_even += element[i]
                #print(element[i])
        print(str_odd+" "+str_even)

        #for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])
