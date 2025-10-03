def get_choice(player):
    choice = input(f"{player}, choose Rock, Paper, or Scissors: ").strip().lower()
    if choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        return get_choice(player)
    return choice

def decide_winner(p1, p2):
    if p1 == p2:
        return "It's a tie!"
    wins = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    if wins[p1] == p2:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play():
    print("🎮 Rock, Paper, Scissors - 2 Player Game")
    p1 = get_choice("Player 1")
    p2 = get_choice("Player 2")
    print(f"\nPlayer 1 chose: {p1.capitalize()}")
    print(f"Player 2 chose: {p2.capitalize()}")
    print(decide_winner(p1, p2))

play()
exit()