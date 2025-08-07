x = ['_'] * 9
t1 = input('write name who is starting: ')
t2 = input('write name of second person: ')
t = t1
while True :
    print(x[0:3])
    print(x[3:6])
    print(x[6:9])
    print(f'it is turn of {t}')
    try:
        ind = int(input("which box do you want to use?(1-9): "))
    except:
        print('wrong choice please choose between 1-9')
        continue
    if x[ind-1] == '_':
        x[ind-1] = t 
    else:
        print('it was already taken so you get another chance!')
        continue

    w = False
    if x[0] == x[1]==x[2]!= '_': w=True
    if x[3] == x[4]==x[5]!= '_': w=True
    if x[6] == x[7]==x[8]!= '_': w=True
    if x[0] == x[3]==x[6]!= '_': w=True
    if x[1] == x[4]==x[5]!= '_': w=True
    if x[6] == x[7]==x[8]!= '_': w=True
    if x[0] == x[4]==x[8]!= '_': w=True
    if x[6] == x[4]==x[2]!= '_': w=True
    if w:
        print('plaeyer won')
        print('player name is ',t)
        break

    if t==t1:
        t = t2
    elif t==t2:
        t = t1
