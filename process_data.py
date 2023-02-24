import pandas as pd

def replace_spaces(csv):
    '''
    Takes in a pandas dataframes and replaces all the space found in the column names (attributes)
    with underscores ('_') while also changing all of it to lower case. This is done to ensure uniformity
    for all column names as well as to allow for easy accessing of columns. Columns can be grabbed by simply
    doing df.attribute where attribute is the name of the columns

    :param: csv
    :type: pd.DataFrame
    '''
    assert isinstance(csv, pd.DataFrame)

    csv.columns = [c.replace(' ', '_').lower() for c in csv.columns]
    return csv

gdp = pd.read_csv('Data/gdp.csv')
gdp = replace_spaces(gdp)


world_cup_matches = pd.read_csv('Data/world_cup_matches.csv')
world_cup_matches = replace_spaces(world_cup_matches)

# Removing countries that weren't in the world cup from all the GDP data
index = gdp.country_name.isin(world_cup_matches.home_team) | gdp.country_name.isin(world_cup_matches.away_team)
print(index)
gdp = gdp[index]
gdp.to_csv('Clean_Data/gdp.csv')

#players
players = pd.read_csv('Data/players_22.csv')
players.nationality_name = players.nationality_name.replace(['China PR', 'Republic of Ireland'], ['China', 'Ireland'])
