inp1 = []
inp = '_________'
for i in inp:
    inp1.append(i)
def display(inp):

    print('-----------')
    print("| ",end = '')
    for i in range(len(inp)):

        if(i > 0 and i % 3 == 0):
            print(" |",end='')
            print("\n")
            print('| ',end='')
            print(inp[i],end=' ')

        else:
            print(inp[i],end=' ')
    print(" |")
    print('-----------')
    return ''

def game(inp):
    display(inp)
    res = 'Draw'
    count_x = inp.count("X")
    count_o = inp.count("O")
    difference = count_x - count_o
    if abs(difference) > 1:
        print('Impossible')
        quit()
    for i in range(len(inp)):
        if inp[i] == "_":
            res = 'Game not finished'
    count = 0

    for i in range(len(inp)):
        if i % 3 == 0:
            if inp[i:i+3] == 'XXX':
                res = 'X wins'
            if inp[i:i+3] == 'OOO':
                res = 'O wins'
    for i in range(len(inp[:3])):
        str = inp[i],inp[i+3],inp[i+6]
        str = ''.join(str)
        if str == 'XXX':
            count += 1
            res = 'X wins'
        if str == 'OOO':
            count += 1
            res = 'O wins'

    for i in range(1):
        str = inp[i],inp[i+4],inp[i+8]
        str = ''.join(str)
        if str == 'XXX':
            res = 'X wins'
        if str == 'OOO':
            res = 'O wins'
    for i in range(1):
        str = inp[i+2],inp[i+4],inp[i+6]
        str = ''.join(str)
        if str == 'XXX':
            res = 'X wins'
        if str == 'OOO':
            res = 'O wins'
    if res == 'Game not finished':
        user(inp)
        quit()
    elif count < 2:
        print(res)
        quit()
    else:
        print('Impossible')
    return ''
def user(inp):
    try:
        u_input = list(map(int,input('Enter the coordinates: ').split()))
        num = 0
        for i in range(2):
            if u_input[i] == ' ':
                u_input.remove(u_input[i])
            if u_input[i] > 3:
                print('Coordinates should be from 1 to 3!')
                user(inp)
                num += 1
        cosum = sum(u_input)
        count_x = inp.count("X")
        count_o = inp.count("O")
        diff = count_x - count_o
        for i in range(1):

            if u_input[i+1] == 1 and num < 1:
                if inp1[cosum+4] == '_':
                    if diff == 0:
                        inp1[cosum+4] = 'X'
                    else:
                        inp1[cosum+4] = 'O'
                else:
                    print('Thsis cell is occupied! Choose another one!')
                    user(inp)
            if u_input[i+1] == 2 and num < 1:
                if inp1[cosum] == '_':
                    if diff == 0:
                        inp1[cosum] = 'X'
                    else:
                        inp1[cosum] = 'O'

                else:
                    print('This cell is occupied! Choose another one!')
                    user(inp)
            if u_input[i+1] == 3 and num < 1:
                if inp1[cosum-4] == '_':
                    if diff == 0:
                        inp1[cosum-4] = 'X'
                    else:
                        inp1[cosum-4] = 'O'
                else:
                    print('This cell is occupied! Choose another one!')
                    user(inp)
        game(inp1)

        #user(inp)

    except ValueError:
        print('You should enter numbers!')
        user(inp)
    return ''




print(game(inp))
