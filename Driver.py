import statsapi

teams = statsapi.get('teams', {'sportId': 1})  # sportId 1 is for MLB

# Loop through the list and print team names with their IDs
for team in teams['teams']:
    print(f"Team: {team['name']}, ID: {team['id']}")