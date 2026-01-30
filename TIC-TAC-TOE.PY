#   Tic tac toe but in python.

'''We will make the board using the dictionary module
the keys will be the location(eg : top-left, mid right, etc)
and initialliy it's values will be empty space and then after every move
we will change the values accordijg to players choice of move.'''

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

'''We will have to reprint the updated board after every move in the game and
thus we will make a function to do that'''

def printBoard(board):
    print(board['7'] + 'l' + board['8'] + 'l' + board['9'])
    print('-+-+-')
    print(board['4'] + 'l' + board['5'] + 'l' + board['6'])
    print('-+-+-')
    print(board['1'] + 'l' + board['2'] + 'l' + board['3'])

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place")


        move = input()
        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. \nMove to another place perhaps")
            continue

        if count >= 5:
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                
                printBoard(theBoard)
                print("\nGame Over. \n")
                print(" **** " +turn + "won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':

                printBoard(theBoard)
                print("\nGame Over. \n")
                print("****" +turn + "won. ***")
                break 
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nGame Over. \n")
                print("****" +turn + "won. ***")
                break 
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nGame Over. \n")
                print("****" +turn + "won. ***")
                break 
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over. \n")
                print("****" +turn + "won. ***")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nGame Over. \n")
                print("****" +turn + "won. ***")
                break 
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nGame Over. \n")
                print("****" +turn + "won. ***")
                break 


            if count == 9:
                print("\nGame Over. \n")
                print("ITS A TIE!!!!!!")

                if turn == 'X':
                      turn = 'O'
                else:
                    turn = 'X'

            restart = input("Do you want to play again?(Yes/No)")
            if restart == "Yes" or restart == "yes":
                for key in board_keys:
                    theBoard[key] = " "
               
               
                game()



if __name__ == "__main__":
    game()



    
 

               
         



