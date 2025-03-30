import random

def play():
    user:str = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie '
      
    # r > s, s > p , p > r
    if is_win(user,computer):
        return 'You won!'

    return 'You lost!'


def is_win(player,opponent):
    # return True if playe?
    if (player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
if __name__ == "__main__":
    main= play()
    print(main)