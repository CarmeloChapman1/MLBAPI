import mlbstatsapi
import requests

mlb = mlbstatsapi.Mlb()

# Get the player ID (e.g., Ty France)
player_id = mlb.get_people_id("Shohei Ohtani")[0]

# Define the stats and groups
stats = ['season']
groups = ['hitting']
params = {'season': 2022}

# Retrieve player stats
player_stats = mlb.get_player_stats(player_id, stats, groups, **params)

# Access hitting stats
hitting_stats = player_stats.get('hitting', {})

if hitting_stats:
    for stat_type, stat_obj in hitting_stats.items():
        print(f"\n{stat_type.capitalize()} Stats:")

        # Access the 'splits' attribute of the Stat object
        splits = stat_obj.splits  # This should be a list of HittingSeason objects

        if splits:
            for split in splits:
                # Access the 'stat' attribute, which contains the actual stats
                stat_data = split.stat

                # Print out the stats from the 'stat' object
                print(f"Games Played: {stat_data.gamesplayed}")
                print(f"Home Runs: {stat_data.homeruns}")
                print(f"RBIs: {stat_data.rbi}")
                print(f"Batting Average: {stat_data.avg}")
                print(f"Hits: {stat_data.hits}")
                print(f"Strikeouts: {stat_data.strikeouts}")
                print(f"Stolen Bases: {stat_data.stolenbases}")
                # Add more stats as needed
        else:
            print("No splits found for this stat type.")
else:
    print("No hitting stats found.")

stats2 = ['season']
groups2 = ['pitching']
params2 = {'season':2022}

ohtani_stats = mlb.get_player_stats(player_id,stats2,groups2, **params2)

pitching_stats = ohtani_stats.get('pitching', {})

if pitching_stats:
  for stat_type, stat_obj in pitching_stats.items():
    print(f"\n{stat_type.capitalize()}")
    
    splits = stat_obj.splits
    
    if splits:
      for split in splits:
        stat_data = split.stat
        print(f"ERA: {stat_data.era}")
        print(f"Strikeouts: {stat_data.strikeouts}")
                # Add more stats as needed
      else:
            print("No splits found for this stat type.")
else:
    print("No hitting stats found.")

