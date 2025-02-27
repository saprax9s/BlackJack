import random as rd
print("Hello would you like to play Blackjack?")
ch = input("y/n: ").lower()
def game():
    p1 = rd.randint(1, 11)
    p2 = rd.randint(1, 11)
    b1 = rd.randint(1, 11)
    b2 = rd.randint(1, 11)
    sp = p1 + p2
    sb = b1 + b2
    if sp == 21:
        print("You win !!Blackjack!!")
    elif sb == 21:
        print("Oops, dealer won by blackjack")
    def valid():
        if sp < 22 and sb < 22:
            if sp > sb:
                print("You Win!!")
                print("Your sum:",sp)
                print("Dealers sum:",sb)
            elif sb > sp:
                print("You Loose")
                print("Your sum:", sp)
                print("Dealers sum:", sb)
            else:
                print("Draw!")
                print("Your sum:", sp)
                print("Dealers sum:", sb)
        elif sp < 22 and sb > 22:
            print("Dealer Bust, Your win!!")
            print("Your sum:", sp)
            print("Dealers sum:", sb)
        elif sp > 22 and sb > 22:
            print("Push!")
            print("Your sum:", sp)
            print("Dealers sum:", sb)
    print("Your cards sum:", sp)
    print("Dealers open card:", b2)
    while sb < 17:
        sb = sb + rd.randint(1, 11)
    for i in range (100):
        print("Hit or Hold?")
        h = input("h(to hit)/H(to hold): ")
        if h == 'H':
            valid()
            break
        elif h == 'h':
            sp = sp + rd.randint(1,11)
            print("Your cards sum:",sp)
            if sp>21:
                print("Oops You Bust")
                break
            elif sp == 21:
                print("You win!!, Blackjack!!")
                break
            else:
                pass
        else:
            print("Invalid Input")
            break
    if input("Wanna play again? (y/n) ").lower == 'y':
        game()
    
if not ch == 'y':
    print("Okay Bye")
elif ch == 'y':
    print("Welcome to Blackjack")
    print("Dealer stands soft at 17 or above")
    game()
else:
    print("Invalid Input")
