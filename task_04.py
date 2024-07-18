print('************* WELCOME TO ROCK-PAPER-SCISSORS GAME ******************')

import random

done = False
wins = 0
losses = 0
ties = 0

names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
loses = {'R': 'P', 'P': 'S', 'S': 'R'}

while not done:
    choice = input('Plz choose your next move(R, P, S) (Q to Quit) : ').upper()
    cpu_choice = random.choice(['R', 'P', 'S'])
    if choice == cpu_choice:
        print(f"It's a tie! You both choose {names[choice]}")
        ties += 1
    elif choice in ['R', 'P', 'S'] :
        if cpu_choice == loses[choice]:
            print(f'CPU wins! you choose {names[choice]}, the CPU choose {names[cpu_choice]}.')
            losses += 1
        else:
            print(f'You wins! you choose {names[choice]}, the CPU choose {names[cpu_choice]}.')
            wins += 1
    elif choice == 'Q':
        done = True
    else:
        print('Invalid command')

    print(f'Current states : {wins} Wins, {losses} Losses, {ties} Ties')