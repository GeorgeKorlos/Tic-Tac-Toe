# Tic Tac Toe
grid = [' ' for _ in range(9)]

def display_grid():
    for i in range(3):
        print('|'.join(grid[i * 3:(i + 1) * 3]))
        if i < 2:
            print('-' * 5)

def player_choice(player):
    while True:
        try:
            choice = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif grid[choice] != ' ':
                print("Cell already taken. Please choose another cell.")
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_winner():

    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    
    for combo in winning_combinations:
        if grid[combo[0]] == grid[combo[1]] == grid[combo[2]] != ' ':
            return grid[combo[0]] 
    
    return None  

def is_draw():
    return ' ' not in grid  

def play_game():
    global grid  
    current_player = 'X'
    
    while True:
        display_grid()
        choice = player_choice(current_player)
        grid[choice] = current_player  
        
        winner = check_winner()
        if winner:
            display_grid()
            print(f"Player {winner} wins!")
            break
 
        if is_draw():
            display_grid()
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    if input("Do you want to play again? (yes/no): ").lower() == 'yes':
        grid = [' ' for _ in range(9)] 
        play_game()  

play_game()
