#閏年の算出
#https://paiza.jp/works/mondai/dateset/leap_year/edit?language_uid=python3


year = int(input())

if year % 4 == 0 :
    if year % 400 == 0:
        print("Yes")
    elif year % 100 == 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")
