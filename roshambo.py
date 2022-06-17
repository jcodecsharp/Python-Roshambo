import random


class Player:
    def __init__(self,player_name,roshambo_value,num_wins,num_losses):
        self.player_name = player_name
        self.roshambo_value = roshambo_value
        self.num_wins = num_wins
        self.num_losses = num_losses


class Bart(Player):
    def __init__(self,player_name,roshambo_value,num_wins,num_losses):
        Player.__init__(self,player_name,roshambo_value,num_wins,num_losses)
        self.player_name = 'Bart'

    def GenerateRoshambo(self):
        self.roshambo_value = 'rock'


class Lisa(Player):
    def __init__(self,player_name,roshambo_value,num_wins,num_losses):
        Player.__init__(self,player_name,roshambo_value,num_wins,num_losses)
        self.player_name = 'Lisa'

    def GenerateRoshambo(self):
        determine = random.randrange(0,3)
        if determine == 0:
            self.roshambo_value = 'rock'
        elif determine == 1:
            self.roshambo_value = 'paper'
        elif determine == 2:
            self.roshambo_value = 'scissors'

def Play(player1,player2,game_count):
    if player1.roshambo_value == 'rock' and player2.roshambo_value == 'rock':
        print(player1.player_name.upper() + ': ' + player1.roshambo_value)
        print(player2.player_name + ': ' + player2.roshambo_value)
        print('DRAW')
    elif player1.roshambo_value == 'rock' and player2.roshambo_value == 'paper':
        print(player1.player_name.upper() + ': ' + player1.roshambo_value)
        print(player2.player_name + ': ' + player2.roshambo_value)
        print('---> ' + player2.player_name.upper() + ' wins!')
        player2.num_wins += 1
        player1.num_losses += 1
    elif player1.roshambo_value == 'rock' and player2.roshambo_value == 'scissors':
        print(player1.player_name.upper() + ': ' + player1.roshambo_value)
        print(player2.player_name + ': ' + player2.roshambo_value)
        print('---> ' + player1.player_name.upper() + ' wins!')
        player1.num_wins += 1
        player2.num_losses += 1
    elif player1.roshambo_value == 'paper' and player2.roshambo_value == 'rock':
        print(player1.player_name.upper() + ': ' + player1.roshambo_value)
        print(player2.player_name + ': ' + player2.roshambo_value)
        print('---> ' + player1.player_name.upper() + ' wins!')
        player1.num_wins += 1
        player2.num_losses += 1
    elif player1.roshambo_value == 'paper' and player2.roshambo_value == 'paper':
        print(player1.player_name.upper() + ': ' + player1.roshambo_value)
        print(player2.player_name + ': ' + player2.roshambo_value)
        print('DRAW')
    elif player1.roshambo_value == 'paper' and player2.roshambo_value == 'scissors':
        print(player1.player_name.upper() + ': ' + player1.roshambo_value)
        print(player2.player_name + ': ' + player2.roshambo_value)
        print('---> ' + player2.player_name.upper() + ' wins!')
        player2.num_wins += 1
        player1.num_losses += 1
    elif player1.roshambo_value == 'scissors' and player2.roshambo_value == 'rock':
        print(player1.player_name.upper() + ': ' + player1.roshambo_value)
        print(player2.player_name + ': ' + player2.roshambo_value)
        print('---> ' + player2.player_name.upper() + ' wins!')
        player2.num_wins += 1
        player1.num_losses += 1
    elif player1.roshambo_value == 'scissors' and player2.roshambo_value == 'scissors':
        print(player1.player_name.upper() + ': ' + player1.roshambo_value)
        print(player2.player_name + ': ' + player2.roshambo_value)
        print('DRAW')
    elif player1.roshambo_value == 'scissors' and player2.roshambo_value == 'paper':
        print(player1.player_name.upper() + ': ' + player1.roshambo_value)
        print(player2.player_name + ': ' + player2.roshambo_value)
        print('---> ' + player1.player_name.upper() + ' wins!')
        player1.num_wins += 1
        player2.num_losses += 1
    print(player1.player_name.upper() + ' total wins: ' + str(player1.num_wins) + '/' + str(game_count)
          +', total lose: ' + str(player1.num_losses) + '/' + str(game_count))
    print(player2.player_name.upper() + ' total wins: ' + str(player2.num_wins) + '/' + str(game_count)
          + ', total lose: ' + str(player2.num_losses) + '/' + str(game_count))

def main():
    game_count = 0
    print('Roshambo Game')
    print()
    your_name = input('Enter your name:')
    player_you = Player(your_name, 'rock', 0, 0)
    print()
    print('Hint 1: Bart\'s Roshambo is always Rock')
    print('Hint 2: Lisa\'s Roshambo is selected by Random')
    print()
    while True:
        choose_player = input('Would you like to play against Bart or Lisa?\n'
        'Type (B/b) for Bart or (L/l) for Lisa: ')
        if choose_player =='l' or choose_player == 'L' or choose_player =='b' or choose_player == 'B':
            break
        else:
            print('Invalid input. Type (B/b) for Bart or (L/l) for Lisa: ')
    print()
    player_bart = Bart('Bart', 'rock', 0, 0)
    player_lisa = Lisa('Lisa', 'rock', 0, 0)
    while True:
        your_choice = input('Rock, paper, or scissors? (r/p/s): ')
        print()
        player_bart.GenerateRoshambo()
        player_lisa.GenerateRoshambo()
        if your_choice == 'r':
            game_count += 1
            player_you.roshambo_value = 'rock'
        elif your_choice == 'p':
            game_count += 1
            player_you.roshambo_value = 'paper'
        elif your_choice == 's':
            game_count += 1
            player_you.roshambo_value = 'scissors'
        else:
            print('Invalid choice. Try again.')
            continue
        if choose_player =='l' or choose_player == 'L':
            Play(player_you,player_lisa,game_count)
        elif choose_player =='b' or choose_player == 'B':
            Play(player_you, player_bart,game_count)
        print()
        play_again = input('Play again? (y/n): ')
        print()
        if play_again == 'n':
            print()
            print('Thanks for playing!')
            break
        

if __name__ == "__main__":
    main()
