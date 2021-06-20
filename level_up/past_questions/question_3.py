#宝くじ
#https://paiza.jp/works/mondai/skillcheck_archive/lottery

b  = int(input())
n  = int(input())

for a in range(n):
    a=int(input())
    if a==b:
        print("first")
    elif a==b-1 or a==b+1:
        print("adjacent")
    elif a%10000 == b%10000:
        print("second")
    elif a%1000 == b%1000:
        print("third")
    else:
        print("blank")
