import pandas as pd

def replace_spaces(csv):
    '''
    '''
    csv.columns = [c.replace(' ', '_') for c in csv.columns]
    return csv

gdp = pd.read_csv('Data/gdp.csv')
gdp = replace_spaces(gdp)

world_cup_matches = pd.read_csv('Data/world_cup_matches.csv')
world_cup_matches = replace_spaces(world_cup_matches)

# Removing countries that weren't in the world cup from all the GDP data
index = gdp.Country_Name.isin(world_cup_matches.Home_Team) | gdp.Country_Name.isin(world_cup_matches.Away_Team)
gdp = gdp[index]

#players
players = pd.read_csv('Data/players_22.csv')
players.nationality_name = players.nationality_name.replace(['China PR', 'Republic of Ireland'], ['China', 'Ireland'])

