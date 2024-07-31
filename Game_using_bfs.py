import random

# Define possible outcomes for each ball
OUTCOMES = [0, 1, 2, 3, 4, 6, 'W']

# Simulate one over of cricket
def play_over(player_decision_function):
    over_result = []
    for _ in range(BALLS_PER_OVER):
        player_decision = player_decision_function()
        if player_decision == 'Y':
            outcome = random.choice(OUTCOMES)
        else:
            outcome = 0  # No run if the player doesn't take the shot
        over_result.append(outcome)
    return over_result

# Simulate an innings for a team
def play_innings(team_name):
    total_score = 0
    wickets = 0
    for over in range(OVERS_PER_TEAM):
        print(f"\n{team_name} is playing over {over + 1}.")
        over_result = play_over(get_player_decision)
        print(f"Over {over + 1} results for {team_name}: {over_result}")
        for ball in over_result:
            if ball == 'W':
                wickets += 1
                print(f"Wicket! {team_name} has lost {wickets} wicket(s).")
                if wickets == PLAYERS_PER_TEAM:
                    print(f"{team_name} is all out!")
                    return total_score, wickets
            else:
                total_score += ball
    return total_score, wickets

# Function to get the player's decision for each ball
def get_player_decision():
    while True:
        decision = input("Do you want to take a shot? (Y/N): ").strip().upper()
        if decision in ['Y', 'N']:
            return decision
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

# Play the cricket match
def play_match():
    print("Welcome to the Cricket Game!")
    
    team1_name = input("Enter the name of Team 1: ")
    team2_name = input("Enter the name of Team 2: ")
    
    global OVERS_PER_TEAM, BALLS_PER_OVER, PLAYERS_PER_TEAM
    OVERS_PER_TEAM = int(input("Enter the number of overs per team: "))
    BALLS_PER_OVER = 6
    PLAYERS_PER_TEAM = int(input("Enter the number of players per team: "))
    
    print(f"\n{team1_name} is batting first.")
    team1_score, team1_wickets = play_innings(team1_name)
    print(f"\n{team1_name} scored {team1_score} runs for {team1_wickets} wickets.")

    print(f"\n{team2_name} is now batting.")
    team2_score, team2_wickets = play_innings(team2_name)
    print(f"\n{team2_name} scored {team2_score} runs for {team2_wickets} wickets.")

    # Determine the winner
    if team1_score > team2_score:
        print(f"\n{team1_name} wins by {team1_score - team2_score} runs!")
    elif team2_score > team1_score:
        print(f"\n{team2_name} wins by {PLAYERS_PER_TEAM - team2_wickets} wickets!")
    else:
        print("\nIt's a tie!")

# Start the game
play_match()
