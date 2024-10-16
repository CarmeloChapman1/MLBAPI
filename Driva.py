import mlbstatsapi
import requests

mlb = mlbstatsapi.Mlb()

player = input(f"Enter a Major League Baseball Player: ")

def PlayerStats(player):

  player_id = mlb.get_people_id(player)[0]

  stats = ['season']
  groups = ['hitting']
  params = {'season': 2024}

  player_stats = mlb.get_player_stats(player_id, stats, groups, **params)

  hitting_stats = player_stats.get('hitting', {})

  if hitting_stats:
    for stat_type, stat_obj in hitting_stats.items():
        print(f"\n{stat_type.capitalize()} Stats:")

        splits = stat_obj.splits

        if splits:
            for split in splits:
              
                stat_data = split.stat

                print(f"Games Played: {stat_data.gamesplayed}")
                print(f"Home Runs: {stat_data.homeruns}")
                print(f"RBIs: {stat_data.rbi}")
                print(f"Batting Average: {stat_data.avg}")
                print(f"Hits: {stat_data.hits}")
                print(f"Strikeouts: {stat_data.strikeouts}")
                print(f"Stolen Bases: {stat_data.stolenbases}\n")
        else:
          print("No hitting stats found.")

  stats2 = ['season']
  groups2 = ['pitching']
  params2 = {'season':2024}

  player_stats = mlb.get_player_stats(player_id,stats2,groups2, **params2)

  pitching_stats = player_stats.get('pitching', {})

  if pitching_stats:
    for stat_type, stat_obj in pitching_stats.items():
      print(f"\n{stat_type.capitalize()}")

      splits = stat_obj.splits

    if splits:
      for split in splits:
        stat_data = split.stat
        print(f"Games Played: {stat_data.gamesplayed}")
        print(f"Games Started: {stat_data.gamesstarted}")
        print(f"ERA: {stat_data.era}")
        print(f"Strikeouts: {stat_data.strikeouts}")
    else:
      print("No Pitching stats found.")

player_stat = PlayerStats(player)

print(player_stat)