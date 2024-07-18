# Инициализация игрового поля
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
Hor = [" ", "1", "2", "3"]
Ver = ["1",
       "2",
       "3"]
# Условия для победы
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

print('Добро пожаловать в игру "Крестики-нолики"')
print()
print("Правила:")
print("1) Первими ходят крестики")
print("2) Игра завершается после того как получается ряд из символов по вертикили, горизонтали или диагонали")
print("3) Чтобы совершить ход необходимо ввести код ячейки: сначала по вертикали потом по горизонтали")
print()
print("Удачной игры")
print()

# Вывод игрового поля на экран
def print_maps():
    print(Hor[0], end=" ")
    print(Hor[1], end=" ")
    print(Hor[2], end=" ")
    print(Hor[3])

    print(Ver[0], end=" ")
    print(board[0], end=" ")
    print(board[1], end=" ")
    print(board[2])

    print(Ver[1], end=" ")
    print(board[3], end=" ")
    print(board[4], end=" ")
    print(board[5])

    print(Ver[2], end=" ")
    print(board[6], end=" ")
    print(board[7], end=" ")
    print(board[8])


# номер ячейки на игровом поле
def get_cell_board(step):
    if step == 11:
        return 0
    elif step == 12:
        return 1
    elif step == 13:
        return 2
    elif step == 21:
        return 3
    elif step == 22:
        return 4
    elif step == 23:
        return 5
    elif step == 31:
        return 6
    elif step == 32:
        return 7
    elif step == 33:
        return 8


# Функция позваоляющая сделать ход
def step_board(step, symbol):
    ind = get_cell_board(step)
    board[ind] = symbol


# Получение результата игры
def get_result():
    win = ""

    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "Крестик"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "Нолик"

    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем поле
    print_maps()

    # 2. Спросим у игрока куда делать ход
    if player1 == True:
        symbol = "X"
        print()
        step = int(input("Игрок №1, ваш ход: "))
    else:
        symbol = "O"
        print()
        step = int(input("Игрок №2, ваш ход: "))

    step_board(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победил", win)
