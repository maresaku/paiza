#一日一万歩
#https://paiza.jp/works/mondai/drankfast/d1_step_distance

line = input().split(" ")

d = int(line[0])
s = int(line[1])

if d*1000*100/s >= 10000:
    print("yes")
else:
    print("no")
