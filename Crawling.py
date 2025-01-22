import requests
from datetime import datetime
import json
import mlbstatsapi

def get_hitter_stat(player):
    selected = ["gamesplayed", "groundouts", "airouts", "runs", "doubles", "triples", "homeruns", "strikeouts", "baseonballs", "intentionalwalks", "hits", "hitbypitch", "avg", "atbats", "obp", "slg", "ops", "caughtstealing", "stolenbases", "stolenbasepercentage", "plateappearances", "sacbunts", "sacflies", "babip", "groundoutstoairouts", "atbatsperhomerun"]
    mlb = mlbstatsapi.Mlb()
    player_id = mlb.get_people_id(player)[0]
    stats = ['season', 'seasonAdvanced']
    groups = ['hitting']
    params = {'season': 2024}
    mlb.get_player_stats(player_id, stats, groups, **params)
    stat_dict = mlb.get_player_stats(player_id, stats=stats, groups=groups, **params)
    season_hitting_stat = stat_dict['hitting']['season']
    string = ""
    for split in season_hitting_stat.splits:
        for k, v in split.stat.__dict__.items():
            if k in selected:
                string += str(k) + ": " + str(v) + "\n"
    return string

def get_pitcher_stat(player):
    selected = ["gamesplayed", "gamesstarted", "groundouts", "airouts", "runs", "doubles", "triples", "homeruns", "strikeouts", "baseonballs", "hits", "hitbypitch", "avg", "atbats", "obp", "slg", "ops", "caughtstealing", "stolenbases", "stolenbasepercentage", "numberofpitches", "inningspitched", "whip", "strikepercentage", "wildpitches", "pickoffs", "groundoutstoairouts", "pitchesperinning", "strikeoutwalkratio", "strikeoutsper9inn", "walksper9inn", "hitsper9inn", "runsscoredper9", "homerunsper9", "sacbunts", "sacflies", "battersfaced"]
    mlb = mlbstatsapi.Mlb()
    player_id = mlb.get_people_id(player)[0]
    stats = ['season', 'seasonAdvanced']
    groups = ['pitching']
    params = {'season': 2024}
    mlb.get_player_stats(player_id, stats, groups, **params)
    stat_dict = mlb.get_player_stats(player_id, stats=stats, groups=groups, **params)
    season_pitching_stat = stat_dict['pitching']['season']
    string = ""
    for split in season_pitching_stat.splits:
        for k, v in split.stat.__dict__.items():
            if k in selected:
                string += str(k) + ": " + str(v) + "\n"
    return string