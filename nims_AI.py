import random

def countpiles():
    print("pile1")

def qlearning(numberofgames, startboard):
    qvalues = {}

    for x in range(0, numberofgames):
##        print(x)
        board = startboard
        while board != "A000"  and board != "B000":
##            print(board)
            a, b, c, d, e, f = board
            if (int(b) == 0 and int(c) != 0 and int(d) != 0):
                pilenumber = random.choice([1,2])
            elif (int(b) != 0 and int(c) == 0 and int(d) != 0):
                pilenumber = random.choice([0,2])
            elif (int(b) != 0 and int(c) !=0 and int(d) == 0):
                pilenumber = random.choice([0,1])
            elif (int(b) != 0 and int(c) == 0 and int(d) == 0):
                pilenumber = 0
            elif (int(b) == 0 and int(c) != 0 and int(d) == 0):
                pilenumber = 1
            elif (int(b) == 0 and int(c) == 0 and int(d) != 0):
                pilenumber = 2
            else:
                pilenumber = random.choice([0,1,2])

##            print("pile " + str(pilenumber+ 1))

            list1 = list(board)
            list1[4] = str(pilenumber)
            board = ''.join(list1)
##            print(board)
            a, b, c, d, e, f = board
            if (pilenumber == 0):
                sizeofpile = b
            if (pilenumber == 1):
                sizeofpile = c
            if (pilenumber == 2):
                sizeofpile = d

##            print("size of pile " + sizeofpile)

            objectstaken = random.randint(1, int(sizeofpile))
##            print("objects taken " + str(objectstaken))
            list2 = list(board)
            list2[5] = str(objectstaken)
            board = ''.join(list2)
##            print(board)

            nextstateboard = (board + '.')[:-1]
##            print(nextstateboard)

            a, b, c, d, e, f = nextstateboard
            if (pilenumber == 0):
                b = str(int(b) - objectstaken)


            if (pilenumber == 1):
                c = str(int(c) - objectstaken)

            if (pilenumber == 2):
                d = str(int(d) - objectstaken)

            if (board[0] == 'A'):
                a = 'B'
            else:
                a = 'A'

            nextstateboard = a + b + c  + d
##            print("next state board " + nextstateboard)

            if (nextstateboard == 'A000'):
                reward = 1000
            elif (nextstateboard == 'B000'):
                reward = -1000
            else:
                reward = 0


            if (board[0] == 'A'):
                if board not in qvalues:
                    qvalues[board] = 0

                minvalue = 1000

                if int(b) > 0:
                    i = 0
                    while i < int(b):
                        nextstateboard = a + b + c + d + '0' + str((int(b)-i))
                        i += 1
##                        print(nextstateboard)
                        if nextstateboard in qvalues:

                            if minvalue > qvalues[nextstateboard]:
##                                print("hello")

                                minvalue = qvalues[nextstateboard]

                if int(c) > 0:
                    i = 0
                    while i < int(c):
                        nextstateboard = a + b + c + d + '1' + str((int(c)-i))
                        i += 1
##                        print(nextstateboard)
                        if nextstateboard in qvalues:
                            if minvalue > qvalues[nextstateboard]:
##                                print("hello")

                                minvalue = qvalues[nextstateboard]

                if int(d) > 0:
                    i = 0
                    while i < int(d):
                        nextstateboard = a + b + c + d + '2' + str((int(d)-i))
                        i += 1
##                        print(nextstateboard)
                        if nextstateboard in qvalues:

                            if minvalue > qvalues[nextstateboard]:
##                                print("hello")

                                minvalue = qvalues[nextstateboard]



                qvalues[board] = (qvalues[board] + (reward + float(.9*(minvalue)) - qvalues[board]))

                board = nextstateboard

##                print("BOARD " + board)

            else:
                if board not in qvalues:
                    qvalues[board] = 0

                maxvalue = -1000

                if int(b) > 0:
                    i = 0
                    while i < int(b):
                        nextstateboard = a + b + c + d + '0' + str((int(b)-i))
                        i += 1
##                        print(nextstateboard)
                        if nextstateboard in qvalues:

                            if maxvalue < qvalues[nextstateboard]:
##                                print("hello")

                                maxvalue = qvalues[nextstateboard]

                if int(c) > 0:
                    i = 0
                    while i < int(c):
                        nextstateboard = a + b + c + d + '1' + str((int(c)-i))
                        i += 1
##                        print(nextstateboard)
                        if nextstateboard in qvalues:


                            if maxvalue < qvalues[nextstateboard]:
##                                print("hello")

                                maxvalue = qvalues[nextstateboard]

                if int(d) > 0:
                    i = 0
                    while i < int(d):
                        nextstateboard = a + b + c + d + '2' + str((int(d)-i))
                        i += 1
##                        print(nextstateboard)
                        if nextstateboard in qvalues:

                            if maxvalue < qvalues[nextstateboard]:
##                                print("hello")
                                maxvalue = qvalues[nextstateboard]



                qvalues[board] = (qvalues[board] + (reward + float(.9*(maxvalue)) - qvalues[board]))

                board = nextstateboard

##                print("BOARD " + board)

    print("Final Q-values:\n")
    for item in qvalues:

        print(item + " " + str(qvalues[item]*10))



    playagain = 1
    gameplayed = 0
    while (playagain == 1):
        if (gameplayed != 0):
            playagain = int(input("\nPlay again? (1) Yes (2) No "))
            if (playagain != 1):
                break
        gameplayed = 1
        board = startboard[:-2]
        firstplayer = int(input("\nWho moves first User (1) or Computer (2)? "))
        if (firstplayer == 1):
            playerturn = 1
        else:
            playerturn = 2


        while board != "A000"  and board != "B000":
            if (playerturn == 1 and firstplayer == 1 or playerturn == 1 and firstplayer == 2):
                if (playerturn == 1 and firstplayer == 1):
                    playerAorB = 'A'
                else:
                    playerAorB = 'B'

                print("\nPlayer " + playerAorB + " (user)'s turn; the board is " + board[1:])
                pilenumber = int(input("What pile do you chose? 0, 1, 2. "))
                while(pilenumber > 2 or pilenumber < 0):
                    print("Invalid. Pick 0, 1 or 2. ")
                    pilenumber = int(input())
                objectsremoved = int(input("How many objects do you want to remove from that pile? "))
                a, b, c, d = board
                if (pilenumber == 0):
                    b = str(int(b) - objectsremoved)

                if (pilenumber == 1):
                    c = str(int(c) - objectsremoved)

                if (pilenumber == 2):
                    d = str(int(d) - objectsremoved)


                if (firstplayer == 1):
                    a = 'B'
                else:
                    a = 'A'


                board = a + b + c + d
                playerturn = 2


            elif (playerturn == 2 and firstplayer == 2):
                print("\nPlayer A (computer)'s turn; board is " + board[1:])
                a, b, c, d = board
                maxqvalue = -1001

                if int(b) > 0:
                    i = 0
                    while i < int(b):
                        nextstateboard = a + b + c + d + '0' + str((int(b)-i))
                        i += 1

                        if (qvalues[nextstateboard] > maxqvalue):
                            maxqvalue = qvalues[nextstateboard]
                            nextboard = nextstateboard



                if int(c) > 0:
                    i = 0
                    while i < int(c):
                        nextstateboard = a + b + c + d + '1' + str((int(c)-i))
                        i += 1
    ##                        print(nextstateboard)
                        if (qvalues[nextstateboard] > maxqvalue):
                            maxqvalue = qvalues[nextstateboard]
                            nextboard = nextstateboard


                if int(d) > 0:
                    i = 0
                    while i < int(d):
                        nextstateboard = a + b + c + d + '2' + str((int(d)-i))
                        i += 1
                        if (qvalues[nextstateboard] > maxqvalue):
                            maxqvalue = qvalues[nextstateboard]
                            nextboard = nextstateboard

                a, b, c, d, e, f = nextboard
                x, y = nextboard[4:]
                print("Computer chooses pile " + x + " and removes " + y + ".")


                if (e == '2'):
                    d = int(d) - int(f)
                elif (e == '1'):
                    c = int(c) - int(f)
                elif (e == '0' ):
                    b = int(b) - int(f)
                nextboard = 'B' + str(b) + str(c) + str(d)


                board = nextboard
                playerturn = 1


            elif (playerturn == 2 and firstplayer == 1):
                print("\nPlayer B (computer)'s turn; board is " + board[1:])

                a, b, c, d = board
                minqvalue = 1001

                if int(b) > 0:
                    i = 0
                    while i < int(b):
                        nextstateboard = a + b + c + d + '0' + str((int(b)-i))
                        i += 1

                        if (qvalues[nextstateboard] < minqvalue):
                            minqvalue = qvalues[nextstateboard]
                            nextboard = nextstateboard


                if int(c) > 0:
                    i = 0
                    while i < int(c):
                        nextstateboard = a + b + c + d + '1' + str((int(c)-i))
                        i += 1
    ##                        print(nextstateboard)
                        if (qvalues[nextstateboard] < minqvalue):
                            minqvalue = qvalues[nextstateboard]
                            nextboard = nextstateboard

                if int(d) > 0:
                    i = 0
                    while i < int(d):
                        nextstateboard = a + b + c + d + '2' + str((int(d)-i))
                        i += 1
                        if (qvalues[nextstateboard] < minqvalue):
                            minqvalue = qvalues[nextstateboard]
                            nextboard = nextstateboard

                a, b, c, d, e, f = nextboard
                x, y = nextboard[4:]
                print("Computer chooses pile " + x + " and removes " + y + ".")


                if (e == '2'):
                    d = int(d) - int(f)
                elif (e == '1'):
                    c = int(c) - int(f)
                elif (e == '0' ):
                    b = int(b) - int(f)
                nextboard = 'A' + str(b) + str(c) + str(d)

                board = nextboard

                playerturn = 1

        if (board == "A000"  or board == "B000"):
            print("\nGame Over.")
            if (board == "A000"):
                print("Winner is player A")
            if (board == "B000"):
                print("Winner is player B")


def main():

    pile1 = int(input("Welcome to Nim\nHow many object do you want in pile 1. Enter: 0 to 3\n"))
    while(pile1 > 3 or pile1 <0):
        pile1 = int(input("Invalid number for pile 1\nEnter new number of objects for pile 1\n"))

    pile2 = int(input("How many object do you want in pile 2. Enter: 0 to 4\n"))
    while(pile2 > 4 or pile2 <0):
        pile2 = int(input("Invalid number for pile 2\nEnter new number of objects for pile 2\n"))

    pile3 = int(input("How many object do you want in pile 3. Enter: 0 to 5\n"))
    while(pile3 > 5 or pile3 <0):
        pile3 = int(input("Invalid number for pile 3\nEnter new number of objects for pile 3\n"))

    numberofgames = int(input("How many games do you want to simulate "))
    while(numberofgames <= 0):
        numberofgames = int(input("Invalid number for number of games you want to simulate\nEnter new number of games you want to simulate greater than 0 "))


##    int(input("How many games do you want to simulate\n"))

    playerturn = 'A'

    """
    str(input("Enter A if you want to go first. B if you want the other person to go first\n"))
    while(playerturn != 'A' and playerturn != 'B'):
        playerturn = str(input("Invalid input.\nEnter A if you want to go first. B if you want the other person to go first.\n"))
    """

##    print(playerturn)
    board = playerturn + str(pile1) + str(pile2) + str(pile3) + '9' + '9'

    print("Initial board is " + str(pile1) + "-" + str(pile2) + "-" + str(pile3) + ", simulating " + str(numberofgames) + " games.\n")

    qlearning(numberofgames, board)

main ()
