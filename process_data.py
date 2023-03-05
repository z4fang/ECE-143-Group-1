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

# Read all CSVs into DataFrames
gdp = pd.read_csv('Data/gdp.csv')
gdp_growth = pd.read_csv('Data/gdp_growth.csv')
gdp_per_capita_growth = pd.read_csv('Data/gdp_per_capita_growth.csv')
gdp_per_capita = pd.read_csv('Data/gdp_per_capita.csv')
gdp_ppp_per_capita = pd.read_csv('Data/gdp_ppp_per_capita.csv')
gdp_ppp = pd.read_csv('Data/gdp_ppp.csv')

world_cup_matches = pd.read_csv('Data/world_cup_matches.csv')
world_cups = pd.read_csv('Data/world_cups.csv')

# Replace all spaces with underscores
gdp = replace_spaces(gdp)
gdp_growth = replace_spaces(gdp_growth)
gdp_per_capita_growth = replace_spaces(gdp_per_capita_growth)
gdp_per_capita = replace_spaces(gdp_per_capita)
gdp_ppp_per_capita = replace_spaces(gdp_ppp_per_capita)
gdp_ppp = replace_spaces(gdp_ppp)

world_cup_matches = replace_spaces(world_cup_matches)
world_cups = replace_spaces(world_cups)

# Removing countries that weren't in the world cup from all the GDP data
index = gdp.country_name.isin(world_cup_matches.home_team) | gdp.country_name.isin(world_cup_matches.away_team)
gdp = gdp[index]
gdp_growth = gdp_growth[index]
gdp_per_capita_growth = gdp_per_capita_growth[index]
gdp_per_capita = gdp_per_capita[index]
gdp_ppp_per_capita = gdp_ppp_per_capita[index]
gdp_ppp = gdp_ppp[index]

# Write the cleaned data back into csv files in Clean_Data folder
gdp.to_csv('Clean_Data/gdp.csv')
gdp_growth.to_csv('Clean_Data/gdp_growth.csv')
gdp_per_capita_growth.to_csv('Clean_Data/gdp_per_capita_growth.csv')
gdp_per_capita.to_csv('Clean_Data/gdp_per_capita.csv')
gdp_ppp_per_capita.to_csv('Clean_Data/gdp_ppp_per_capita.csv')
gdp_ppp.to_csv('Clean_Data/gdp_ppp.csv')

# Write world_cup_matches into csv as all_world_cup_matches
world_cup_matches.to_csv('Clean_Data/all_world_cup_matches.csv')

# Write world_cups into csv as all_world_cup_winners
world_cups.to_csv('Clean_Data/all_world_cup_winners.csv')
