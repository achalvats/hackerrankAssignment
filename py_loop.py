def todo(n):
    li=[]
    if(n>0 and n<21):
        for i in range(0,n):
            #print(i*i)
            li.append(i*i)
    return li

if __name__ == '__main__':
    n = int(input())
    ans=[]
    ans=todo(n)
    for an in ans:
        print(an)
