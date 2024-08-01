import ast
import random
import json
random.seed()

PLAYER = "X"
COMPUTER = "O"
mark = None
score = 0
'''
    These are important variables that are needed in the program and i also
    imported modules i will be using later on
'''
def draw_board(board):
    # develop code to draw the board
    '''
        This function creates the board where the game would be played
        I used two for loops to create the board
    '''
    for i in range(3):
        print("+---+---+---+")
        print("|", end = "")
        for j in range(3):
            print("", board[i][j], end = " |")
        print("\n+---+---+---+")

def welcome(board):
    # prints the welcome message
    # display the board by calling draw_board(board)
    '''
        This function prints out a welcome message when the program is run and
        it calls the draw board function
    '''
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print('The board layout is shown below:')
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want")

def initialise_board(board):
    # develop code to set all elements of the board to one space ' '
    '''
        This function intialises the board, it turns all the values in board
        into single space
    '''
    board = [ [' ',' ',' '],\
              [' ',' ',' '],\
              [' ',' ',' ']]
    return board


def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    '''
        This function gets the player move and adds it to the board and
        it catches all the error the player might make
    '''
    while True:
        choice = input("Choose your square: ")
        if choice == "q":
            raise Exception("Player quits the game")
        if choice.isdigit():
            choice = int(choice)
            if choice >= 1 and choice <= 9:
                row = (choice - 1) // 3
                col = (choice - 1) % 3
                if board[row][col] == " ":
                    break
                print("Square not empty")
            else:
                print("Square number must be between 1 and 9")
        else:
            print("Input must be a number")
    board[row][col] = PLAYER
    #draw_board(board)
    return row, col


def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    '''
        This function gets the computer move and makes sure the location is empty
    '''
    while True:
        row = random.randint(1,3) - 1
        col = random.randint(1,3) - 1
        if board[row][col] == " ":
            board[row][col] = COMPUTER
            break
        continue
    draw_board(board)
    return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    '''
        This function checks for all the possible winning outcomes on the board
        which includes horizontal, vertical and diagonal returning true
    '''
    if board[0][0] == board[0][1] == board[0][2] and board[0][1] != " ":
        mark = board[0][0]
        return True
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ":
        mark = board[1][0]
        return True
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
        mark = board[2][0]
        return True
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
        mark = board[0][0]
        return True
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
        mark = board[0][1]
        return True
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
        mark = board[0][2]
        return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        mark = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        mark = board[0][2]
        return True
    else:
        return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    '''
        This function checks for draw in the board. If a cell is empty, it
        returns false and if not, returns true. I used 2 for loops which
        means it will check every cell of the board
    '''
    for row in range(0,3):
        for col in range(0,3):
            if board[col][row] ==  " ":
                return False
    return True

def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
    '''
        This function is where all the functions come together and they are called
        The board is initialised at first and then using a while loop i get the
        player move, check for a win, check for a draw and then do the same for
        the computer. This is repeated until one of the condition is met
    '''
    global score
    board = initialise_board(board)
    draw_board(board)
    while True:
        get_player_move(board)
        if check_for_win(board,mark):
            draw_board(board)
            print("You win")
            return 1
        if check_for_draw(board):
            draw_board(board)
            print("It's a draw")
            return 0
        choose_computer_move(board)
        if check_for_win(board,mark):
            draw_board(board)
            print("You lose!")
            return -1
        if check_for_draw(board):
            draw_board(board)
            print("It's a draw")
            return 0


def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    '''
        The menu function gets the player input which decides what function
        will run next
    '''
    print("Enter one of the following options: \n \t 1 - Play the game")
    print("\n \t 2 - Save your score in the leaderboard")
    print("\n \t 3 - Load and display the leaderboard")
    print("\n \t q - End the problem")
    choice = input("1, 2, 3 or q? ")
    return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    '''
        I opened the leaderboard file, and then passed the contents of the
        file into leader and then returned leader
    '''
    global leaders
    with open("leaderboard.txt") as f:
        leaders = f.read()
        leaders = ast.literal_eval(leaders)
    return leaders

def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    '''
        For this function, i asked the player for their name, i opened the
        leaderboard file and read its contents and then copied all its contents
        into the variable "save". I turned the variable which is a string into
        a dictionary, created a for loop that checks whether the user already
        exists in the leaderboard and if yes, it updates their score and if the
        user isnt on the leaderboard, it updates the dictionary with the new
        name and score. I then opened the leaderboard file again but this time
        in write mode and then used json to dump the dictionary into the file
    '''

    name = input("What is your name? ")
    while not name.isalpha():
        print("Name must only include alphabets")
        name = input("What is your name? ")
    f = open("leaderboard.txt", "r")
    save = f.read()
    save = ast.literal_eval(save)
    for key in save.copy():
        if key == name:
            save[name] = score
        else:
            save.update({name : score})
    f.close
    file = open("leaderboard.txt","w")
    file.write(json.dumps(save))
    file.close
    print("Score {} for {} saved".format(score,name))


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    '''
        I created 2 print statement that says what this function does
        once it is ran, and then opened the leaderboard file, took it's
        contents and formatted them to be appropriate to see
    '''

    print("The current leaderboard is: ")
    print("\t Name \t Score")
    with open("leaderboard.txt") as file:
        a = file.read()
        a = ast.literal_eval(a)
        for k, v in a.items():
            print("\t" + "{} \t {}".format(k,v))
