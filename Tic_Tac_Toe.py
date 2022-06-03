def main():
    board=make_board()
    print("-----------------------------------------------------\nWelcome to TicTacToe! This game is for 2 but we're devs so lets pretend to have friends!\nFollow the prompts to play, type q at any time to quit")
    p1 = Player()
    p2=Player()
    start_game(p1,p2)
    #print(f"player 1's global{vars(p1)}")
    display(board)
    for x in range (0,9):
        if p1.get_turn():
            play(p1,board)
            p2.set_turn(True)
        elif p2.get_turn():
            play(p2,board)
            p1.set_turn(True)


def start_game(p1,p2):
    print("\nPlayer 1, choose your symbol (X or O)\n")
    p1.set_mark(choose_symbol())
    if p1.get_mark()=='X':
        p2.set_mark('O')
        p1.set_turn(True)
        print("\nX starts first so player 1 goes")
    else:
        p2.set_mark('X')
        p2.set_turn(True)
        print("\nX starts first so player 2 goes")
     #printing the values stored in an object, for tracing, remove after
    #print(f"player 1's inner{vars(p1)}")

def make_board():
    '''
    the board is a dictionnary so that player can enter a coordinate intuitively and
    place their marks, I got the idea from battleship which could be a project in 
    the future, maybe in C
    '''
    board = {}
    for char in 'abc':
        for x in range(1,4):
            board[f'{char}{x}']=''
    return board
    #print(board)

def choose_symbol():
    out=''
    while True:
        out=input("enter X or O ->")
        if out == 'q':
            print("thank you for playing!")
            quit()
        elif out.upper() in ('X','O'):
            return out.upper()
    

def display(board):
    print("\n\t1\t\t2\t\t3")
    print("  ----------------------------------------------")
    print(" |\t\t|\t\t|\t\t|")
    print(f"a|\t{board['a1']}\t|\t{board['a2']}\t|\t{board['a3']}\t|")
    print(" |\t\t|\t\t|\t\t|")
    print("  ----------------------------------------------")
    print(" |\t\t|\t\t|\t\t|")
    print(f"b|\t{board['b1']}\t|\t{board['b2']}\t|\t{board['b3']}\t|")
    print(" |\t\t|\t\t|\t\t|")
    print("  ----------------------------------------------")
    print(" |\t\t|\t\t|\t\t|")
    print(f"c|\t{board['c1']}\t|\t{board['c2']}\t|\t{board['c3']}\t|")
    print(" |\t\t|\t\t|\t\t|")
    print("  ----------------------------------------------")
    print('\n')

#good old OOP
class Player:
    def __init__(self,mark='',turn=False):
        self._mark=mark
        self._turn=turn

    def set_mark(self,mark):
        self._mark=mark

    def set_turn(self,turn):
        self._turn=turn

    def get_mark(self):
        return self._mark
    def get_turn(self):
        return self._turn

def play(p,board):
    place_mark(p,board)
    display(board)
    if check_win(p,board):
        print(f"{p.get_mark()} won, play again?")
        play_again()
    p.set_turn(False)

def place_mark(p,board):
    while True:
        out=input(f"enter where you want to place {p.get_mark()} (a1 would be top left), q to quit->")
        if (out in board.keys()) and board[out]=='':
            board[out]=p.get_mark()
            break
        elif out=='q':
            print("\nthanks for playing!")
            quit()
        else:
            print("\nlocation is either full or invalid, try again\n")

def check_win(p,board):
    return ((p.get_mark() == board['a1'] == board['a2'] == board['a3']) or # across the top
    (p.get_mark() ==  board['b1'] == board['b2'] == board['b3']) or # across the middle
    (p.get_mark() ==  board['c1'] == board['c2'] == board['c3']) or # across the bottom
    (p.get_mark() ==  board['a1'] == board['b1'] == board['c1']) or # down the left
    (p.get_mark() == board['a2'] == board['b2'] == board['c2']) or # down the middle
    (p.get_mark() ==  board['a3'] == board['b3'] == board['c3']) or # down the right side
    (p.get_mark() ==  board['a1'] == board['b2'] == board['c3']) or # diagonal
    (p.get_mark() ==  board['a3'] == board['b2'] == board['c1'])) # diagonal

def play_again():
    again=input("enter y to continue, anything else to quit ->")
    if again == 'y':
        main()
    else:
        print("\nthanks for playing!")
        quit()

main()


