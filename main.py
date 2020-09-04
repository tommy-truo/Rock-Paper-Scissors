import random


won = 0
lost = 0
tied = 0


def chose_rock():
  global won, lost, tied
  
  player_choice = input("\n\nWhat will you choose?\n\n[1. Rock, 2. Paper, 3. Scissors]\n>>>> ")

  while player_choice.lower() not in ['1', 'rock', '2', 'paper', '3', 'scissors']:
    print("\n\nThat is not an option.\n\n")

    player_choice = input("\n\nWhat will you choose?\n\n[1. Rock, 2. Paper, 3. Scissors]\n>>>> ")

  if player_choice.lower() in ['1', 'rock']:
    print("\n\nYou chose ROCK and the computer chose ROCK!\n\nIt's a tie!")

    tied += 1

  elif player_choice.lower() in ['2', 'paper']:
    print("\n\nYou chose PAPER and the computer chose ROCK!\n\nYou win!")

    won += 1

  elif player_choice.lower() in ['3', 'scissors']:
    print("\n\nYou chose SCISSORS and the computer chose ROCK!\n\nYou lose!")

    lost += 1


def chose_paper():
  global won, lost, tied
  
  player_choice = input("\n\nWhat will you choose?\n\n[1. Rock, 2. Paper, 3. Scissors]\n>>>> ")

  while player_choice.lower() not in ['1', 'rock', '2', 'paper', '3', 'scissors']:
    print("\n\nThat is not an option.\n\n")

    player_choice = input("\n\nWhat will you choose?\n\n[1. Rock, 2. Paper, 3. Scissors]\n>>>> ")

  if player_choice.lower() in ['1', 'rock']:
    print("\n\nYou chose ROCK and the computer chose PAPER!\n\nYou lose!")

    lost += 1

  elif player_choice.lower() in ['2', 'paper']:
    print("\n\nYou chose PAPER and the computer chose PAPER!\n\nIt's a tie!")

    tied += 1

  elif player_choice.lower() in ['3', 'scissors']:
    print("\n\nYou chose SCISSORS and the computer chose PAPER!\n\nYou win!")

    won += 1


def chose_scissors():
  global won, lost, tied
  
  player_choice = input("\n\nWhat will you choose?\n\n[1. Rock, 2. Paper, 3. Scissors]\n>>>> ")

  while player_choice.lower() not in ['1', 'rock', '2', 'paper', '3', 'scissors']:
    print("\n\nThat is not an option.\n\n")

    player_choice = input("\n\nWhat will you choose?\n\n[1. Rock, 2. Paper, 3. Scissors]\n>>>> ")

  if player_choice.lower() in ['1', 'rock']:
    print("\n\nYou chose ROCK and the computer chose SCISSORS!\n\nYou win!")

    won += 1

  elif player_choice.lower() in ['2', 'paper']:
    print("\n\nYou chose PAPER and the computer chose SCISSORS!\n\nYou lose!")

    lost += 1

  elif player_choice.lower() in ['3', 'scissors']:
    print("\n\nYou chose SCISSORS and the computer chose SCISSORS!\n\nIt's a tie!")

    tied += 1


def game():
  global won, lost, tied
  
  available_choices = ('rock', 'paper', 'scissors')
    
  possibilities = {
    'rock' : chose_rock,
    'paper' : chose_paper,
    'scissors' : chose_scissors
    }
    
  com_choice = random.choice(available_choices)
    
  possibilities[com_choice]()

  print("\n\nGames Won : " + str(won) + "\nGames Lost : " + str(lost) + "\nGames Tied : " + str(tied))

  replay = input("\n\nDo you want to play again?\n\n[y/n]\n>>>> ")

  while replay.lower() not in ['y', 'n']:
    print("\n\nThat is not an option.\n\n")

    replay = input("\n\nDo you want to play again?\n\n[y/n]\n>>>> ")

  if replay.lower() == 'n':
    print("\n\nUnderstandable, have a great day.")

  elif replay.lower() == 'y':
    game()


def start_game():
  game_start = input("Would you like to play Rock, Paper, Scissors?\n\n[y/n]\n>>>> ")

  while game_start.lower() not in ['y', 'n']:
    print("\n\nThat is not an option.\n\n")

    game_start = input("Do you want to play Rock, Paper, Scissors?\n\n[y/n]\n>>>> ")

  if game_start.lower() == 'n':
    print("\n\nUnderstandable, have a great day.")

  elif game_start.lower() == 'y':
    game()


def main():
  start_game()


if __name__ == "__main__":
  main()