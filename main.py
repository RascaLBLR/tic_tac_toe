import os
from datetime import datetime
cdt  = datetime.now().strftime("%d.%m.%Y %H:%M")
the_board = [i for i in range (1, 10)]
menu_answers = {"1": "1", "2": "2"}
is_the_user_x = True
TURNS = {True: "X", False: "O"}

def cls():
    if os.name == "nt":
        os.system("cls") 
    else:
        os.system("clear")

def get_answer():
    answer = input("Your choise: ")
    return menu_answers.get(answer)

def statistic_menu():
    cls()
    print("1. Show log of the games")
    print("2. Show statistic of wins\n")
    answer = get_answer()
    while not answer:
        print("Pls peek the right option")
        answer = get_answer()
    return answer

def show_menu():
    cls()
    print("___MENU___")
    print("1. Show statistic")
    print("2. Play the game\n")

    answer = get_answer()
    while not answer:
        print("Pls peek the right option")
        answer = get_answer()
    return answer

def show_the_board():
    cls()
    print(f"{the_board[0]} | {the_board[1]} | {the_board[2]}")
    print("--|---|--")
    print(f"{the_board[3]} | {the_board[4]} | {the_board[5]}")
    print("--|---|--")
    print(f"{the_board[6]} | {the_board[7]} | {the_board[8]}")

def show_statistic():
    answer = statistic_menu()
    cls()
    if answer == "1":
        with open("log.txt", "r") as file:
            print(file.read())
    else:
        with open("log.txt", "r") as file:
            xwin = 0
            owin = 0
            draw = 0
            file.seek(0)
            for line in file:
                if "Player X win!" in line:
                    xwin += 1
                elif "Player O win!" in line:
                    owin += 1
                elif "Draw!" in line:
                    draw += 1
        print("Number of games the player X has won: " , xwin)
        print("Number of games the player O has won: " , owin) 
        print("Number of draws: " , draw)         

def get_user_turn(): 
    while True:
        turn = input(f"User {TURNS.get(is_the_user_x)} turn (1-9): ")  
        try:
            if int(turn) in the_board:  
                return turn
            else:
                print("Enter correct value")
        except:
            print("Enter correct value")

def check_free_cells():
    free = 0
    for i in the_board:
        if i == "X" or i == "O":
            free += 1
    if free == 9:
        return True
    else:
        return False
        
def change_player():
    global is_the_user_x
    is_the_user_x = not is_the_user_x

def check_won():
    if the_board[0] == the_board[1] == the_board[2]:
        return False
    if the_board[3] == the_board[4] == the_board[5]:
        return False
    if the_board[6] == the_board[7] == the_board[8]:
        return False
    if the_board[0] == the_board[3] == the_board[6]:
        return False
    if the_board[1] == the_board[4] == the_board[7]:
        return False
    if the_board[2] == the_board[5] == the_board[8]:
        return False
    if the_board[0] == the_board[4] == the_board[8]:
        return False
    if the_board[2] == the_board[4] == the_board[6]:
        return False
    else:
        return True

def play_the_game():
    show_the_board()
    while True:
        if check_free_cells() and check_won():
            show_the_board()
            with open("log.txt", "a+") as file:
                file.write(f"{cdt} - Draw!\n")
            return print("Draw!")

        elif not check_free_cells():
            turn = get_user_turn()
            the_board[int(turn) - 1] = TURNS.get(is_the_user_x)
            show_the_board()
            if not check_won():
                with open("log.txt", "a+") as file:
                    file.write(f"{cdt} - Player {TURNS.get(is_the_user_x)} win!\n")
                return print(f"Player {TURNS.get(is_the_user_x)} Win!")                    
            change_player()
       
def main():
    answer = show_menu()
    if answer == "1":
        show_statistic()
    else:
        play_the_game()

if __name__ == "__main__":
    main()