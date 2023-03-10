# ECE-143-Group-1

Structural Tasks
- Set up Github repository
- Get all data into pandas dataframes

Cleaning Tasks
- Match players listed in Historical Data on Soccer Players with their world cup team (possible that some players may not be on world cup teams) :heavy_check_mark:
- Filter countries found in World GDP to only countries found in world cup :heavy_check_mark:
- Replace spaces in attribute names to underscores (‘_’) to make it easier for querying :heavy_check_mark:
- Make sure that the country names are consistent e.g. some DataFrames label South Korea as Korea Republic :heavy_check_mark:
- Drop player data columns that are not relevant (mostly ones that relate to on field subjects) (can be changed if needed) :heavy_check_mark:

Cleaned Data:
- all_world_cup_matches: contains all world cup matches that have been played from 1930 to 2018
- all_world_cup_winners: contains all world cup winners from 1930 to 2022
- countries_in_worldcup_18-22: contains all the countries in world cup from 2018 - 2022
- gdp: contains all gdp per year from 1960 to 2020*
- gdp_growth: contains all gdp growth per year from 1960 to 2020*
- gdp_per_capita: contains all gdp per capita per year from 1960 to 2020*
- gdp_per_capita_growth: contains all gdp per capita growth per year from 1960 to 2020*
- gdp_ppp: contains all gdp ppp per year from 1960 to 2020*
- gdp_ppp_per_capita: contains all gdp ppp per capita per year from 1960 to 2020*
- player: contains all the players that are in the team in world cup from 2018 - 2022
- win_loss_goals_30_22: contains number of wining, losing, and goals of each team in each stage before 2022. 

*(limited to only countries that have appeared in the world cup)

Analysis Tasks (Brainstorming)
- The number of times of each country that joins the world cup since 1930
- The number of times of each country that makes it into the Round 16, Quarter-finals, Semi-finals, finals
- The number of goals of each country
- The times of winining and losing in each stage. 
- The trend of wining and losing v.s. GDP for some selected country . 
- The trend of each country’s ranking since 1930 (Might need more data from FIFA or kaggle)
- The population of some countries v.s. their winning rate
- Each countries’ national team players total wages v.s. Their winning rate
- Analysis of 2022 world champion Argentina’s match games (The statistical number when Argentina meets high ranking teams v.s. lower ranking teams)


Insights for visualization: <br>
Data regarding countries:
- Geographical Heat map
- Sector Chart <br>

Data regarding correlation:
- Scatter plot
- Histogram (marginal histogram)
- Correllogram 
https://www.python-graph-gallery.com/
