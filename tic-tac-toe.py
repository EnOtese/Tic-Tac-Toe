def check_winner():
    if screen[0][0] == "X" and screen[0][1] == "X" and screen[0][2] == "X":
        return 'X'
    if screen[1][0] == "X" and screen[1][1] == "X" and screen[1][2] == "X":
        return 'X'
    if screen[2][0] == "X" and screen[2][1] == "X" and screen[2][2] == "X":
        return 'X'
    if screen[0][0] == "X" and screen[1][0] == "X" and screen[2][0] == "X":
        return 'X'
    if screen[0][1] == "X" and screen[1][1] == "X" and screen[2][1] == "X":
        return 'X'
    if screen[0][2] == "X" and screen[1][2] == "X" and screen[2][2] == "X":
        return 'X'
    if screen[0][0] == "X" and screen[1][1] == "X" and screen[2][2] == "X":
        return 'X'
    if screen[0][2] == "X" and screen[1][1] == "X" and screen[2][0] == "X":
        return 'X'
    if screen[0][0] == "0" and screen[0][1] == "0" and screen[0][2] == "0":
        return '0'
    if screen[1][0] == "0" and screen[1][1] == "0" and screen[1][2] == "0":
        return '0'
    if screen[2][0] == "0" and screen[2][1] == "0" and screen[2][2] == "0":
        return '0'
    if screen[0][0] == "0" and screen[1][0] == "0" and screen[2][0] == "0":
        return '0'
    if screen[0][1] == "0" and screen[1][1] == "0" and screen[2][1] == "0":
        return '0'
    if screen[0][2] == "0" and screen[1][2] == "0" and screen[2][2] == "0":
        return '0'
    if screen[0][0] == "0" and screen[1][1] == "0" and screen[2][2] == "0":
        return '0'
    if screen[0][2] == "0" and screen[1][1] == "0" and screen[2][0] == "0":
        return '0'
    return '*'



def draw_screen():
    for i in screen:
        print(*i)


screen = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Добро пожаловать в крестики-нолики!')
print('-----------------------------------')
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестки')
    row = int(input("Введите номер строки (1,2,3) ")) - 1
    column = int(input("Введите номер столбца (1,2,3) ")) - 1
    if screen[row][column] == "*":
        screen[row][column] = turn_char
    else:
        print('Ячейка уже занята, вы пропускаете ход')
        draw_screen()
        continue

    draw_screen()

    if check_winner() == 'X':
        print('Крестики победили!')
        break
    if check_winner() == '0':
        print('Нолики победили!')
        break
    if check_winner() == '*' and turn == 9:
        print('Ничья!')
        break
