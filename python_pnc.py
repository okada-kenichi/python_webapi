def pnc(num):
    count = 0
    for i in (2,num):
        if num%i == 0:
            count = count = 1
    if count == 0:
        print(num)
    return

pnc(11)