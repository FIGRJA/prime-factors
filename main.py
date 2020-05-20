print ('prime_factors')
EE = True
while EE:
    ww = True
    w1 = input(':')
    w1 = int(w1)
    w2 = 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
    w3 = 0
    i = 0
    while ww:
        if  i != 25:
            w3 = w1 % w2[i]
            if w3 == 0:
                print(w1 , '    ' , w2[i])
                w1 = w1 / w2[i]
                w1 = int(w1)
            else:
                i += 1
        elif i == 25:
            ww = False
    print(w1)
    RR = input('ещё?(да/нет)')
    if RR == 'да':
        print('RESTART PROGRAMM')
    elif RR == 'нет':
        EE = False
        print('EXIT')
