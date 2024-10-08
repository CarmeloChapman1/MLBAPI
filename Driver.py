import statsapi
from datetime import datetime, timedelta

teams = statsapi.get('teams', {'sportId': 1})  # sportId 1 is for MLB

# Loop through the list and print team names with their IDs
for team in teams['teams']:
    print(f"Team: {team['name']}, ID: {team['id']}")



today = datetime.now().strftime('%Y-%m-%d')

start_date = '2018-01-01'

schedule = statsapi.schedule(start_date=start_date, end_date=today,sportId=1)
"""
# Loop through the schedule and print the game IDs (boxscore IDs)
for game in schedule:
    print(f"Game: {game['game_id']}, Date: {game['game_date']}, Home: {game['home_name']}, Away: {game['away_name']}")

#print(statsapi.boxscore(775323))
"""
print()
# Example team ID for the New York Yankees (you can replace this with any team ID)
team_id = 147  # New York Yankees team ID

# Retrieve the roster for the team
roster = statsapi.roster(team_id)

print(roster) 

print("")

for player in roster:
    player_name = player['name']  # Assuming 'name' is a valid key based on your printout
    player_id = player['id']  # Assuming 'id' is a valid key to get the player's ID
    
    # Fetch player stats (this can be customized for specific seasons or stat types)
    stats = statsapi.player_stats(player_id, group='hitting', type='season')  # Example: Hitting stats for current season
    
    # Print player name and stats (customize stats output as needed)
    print(f"Player: {player_name}")
    print(f"Stats: {stats}")
    print('-' * 40)