board = []

# Процедура создания списка для поля
def create_board(board):
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)

# Функция регистрации выбранного значения в списке поля
def fix_spot(board, row, col, player):
    if board[row][col] == "X" or board[row][col] == "O":
        result = 0
    else:
        board[row][col] = player
        result = 1
    return result

# Функция проверки победы
def chek_win(board, player):
    win = None

    n = len(board)

    # Строки
    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    # Колонки
    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    # Диагонали
    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

    for row in board:
        for item in row:
            if item == '-':
                return False
    return True

# Функция проверки остатка возмохных ходов
def is_board_filled(board):
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True

# Процедура вывода поля в консоль
def show_board(board):

    import copy
    copy_board = copy.deepcopy(board)
    copy_board.insert(0,[' ','1','2','3'])
    a = 0
    for row in copy_board:
        if a > 0:
            row.insert(0,a)
        a = a + 1
        for item in row:
            print(item, end=" ")
            # print(a)
        print()

def start(board):
    create_board(board)
    player = 'X'
    while True:
        print(f"Ход игрока {player}.")

        show_board(board)

        row, col = list(
            map(int, input("Введите номер строки и колонки через пробел: ").split()))
        print()

        result = fix_spot(board, row - 1, col - 1, player)
        if result == 0 :
            print("Клетка занята")

        if is_player_win(board, player):
            print(f"Игрок {player} выиграл")
            break

        if is_board_filled(board):
            print("Ничья")
            break

        if result == 1:
            player = 'X' if player == 'O' else 'O'

    print()
    show_board(board)

start(board)