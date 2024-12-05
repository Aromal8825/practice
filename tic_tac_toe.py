# tic tac toe #
board = [i for i in range(1, 10)]
used_locations = []

def print_table():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def game():
    count = 0
    player = "X"
    for i in range(10):
        print_table()
        print(f"\n{player}'s chance")
        location = int(input("enter your location : "))
        count += 1
        if location in used_locations:
            print("used location ")
            continue
        if location > 9 or location < 1:
            print("invalid location ")
        board[location - 1] = player
        used_locations.append(location)
        if (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]):
            print(f"{player} wins ")
            print_table()
            break
        elif(count > 8):
            print("draw\n")
            print_table()
            break
        player = "O" if player == "X" else "X"
        
game()
