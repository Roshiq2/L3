import time
import threading

stop_threads = False

def play_game0():
    
    while not stop_threads:
        board = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]

        undo_stack = []

        redo_stack = []

        def print_board():
            print(board[0] + " | " + board[1] + " | " + board[2])
            print(board[3] + " | " + board[4] + " | " + board[5])
            print(board[6] + " | " + board[7] + " | " + board[8])

        def take_turn(player):
            print(player + "'s turn.")
            move = input("Enter a position from 1-9, or 'u' for undo, 'r' for redo: ")
            if move == 'u':
                undo()
            elif move == 'r':
                redo()
            else:
                position = move
                while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    position = input("Invalid input. Choose a position from 1-9: ")
                position = int(position) - 1
                while board[position] != "-":
                    position = int(input("Position already taken. Choose a different position: ")) - 1
                undo_stack.append(list(board))
                board[position] = player
                print_board()

        def undo():
            if undo_stack:
                redo_stack.append(list(board))
                board[:] = undo_stack.pop()
                print_board()
            else:
                print("Cannot undo, no previous moves!")

        def redo():
            if redo_stack:
                undo_stack.append(list(board))
                board[:] = redo_stack.pop()
                print_board()
            else:
                print("Cannot redo, no next moves!")

        def check_game_over():
            if (board[0] == board[1] == board[2] != "-") or \
            (board[3] == board[4] == board[5] != "-") or \
            (board[6] == board[7] == board[8] != "-") or \
            (board[0] == board[3] == board[6] != "-") or \
            (board[1] == board[4] == board[7] != "-") or \
            (board[2] == board[5] == board[8] != "-") or \
            (board[0] == board[4] == board[8] != "-") or \
            (board[2] == board[4] == board[6] != "-"):
                return "win"
            elif "-" not in board:
                return "tie"
            else:
                return "play"

        def play_game():
            print_board()
            current_player = "X"
            game_over = False
            while not game_over:
                take_turn(current_player)
                game_result = check_game_over()
                if game_result == "win":
                    print(current_player + " wins!")
                    game_over = True
                elif game_result == "tie":
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
        play_game()
    else:
        print("draw")


def countdown(t):
    global stop_threads
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # print(timer, end="\r")
        print()
        print(f'-----------------Remaining time: {timer}------------------')
        time.sleep(10)
        t -= 10
        
    stop_threads=True
    print('Timer completed!')


t = 20
thread = threading.Thread(target=countdown, args=(t,))
thread.start()
thread1 =threading.Thread(target=play_game0)
thread1.start()
