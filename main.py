import random

def play():
    user = input("Whats your choice 'r' for rock, 's' for scissors and 'p'for paper\n")
    computer = random.choice(['r' , 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user,computer):
        return 'You won!'
    
    return 'You lost!'
    
def is_win(player, computer):
    # r>s , s>p , p>r
    if(player =='r' and computer== 's') or (player== 's' and computer =='p') or (player=='p' and computer == 'r'):
        return True
    
print(play()) 