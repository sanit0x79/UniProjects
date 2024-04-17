from random import choice

def is_win(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or (player == 'paper' and opponent == 'rock') or (player == 'scissors' and opponent == 'paper'):
        return True
    return False

def play():
    user = input("Choose your weapon: 'rock', 'paper', or 'scissors': ")
    user = user.lower()
    computer = choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return 'It\'s a tie!'

    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'


print(play())