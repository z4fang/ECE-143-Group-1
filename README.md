# ECE_143_Group_1 FIFA World cup Data Analysis and Visualization



The success of a team in the World Cup can be determined by various factors. Understanding these factors and how they impact the winning rate of a team is critical for fans, teams, media outlets, and stakeholders in the world of sports. In this project, we propose to analyze data from the World Cup, focusing on how various factors such as the representative country’s GDP, growth, etc. affect a team’s winning rate. 
 <br>
 <br>
  In the past there were many analysis done based on the game statistics. In our project we want to analyze not just the game statistics but also some other factors like GDP, Club wages, player age etc. 



# File Structure
```
├── Clean_Data
│   ├── all_world_cup.csv
│   ├──countries_in_worldcup_18-22.csv
│   ├── gdp.csv
│   ├── ...    
│   ├── player.csv
│   └── win_loss_goals_30_22.csv
├── Data
│   ├── Player
        ├── nationality.csv
        ├── player_15.csv
        ├── ...
        ├── player_22.csv
│   ├── 2022_world_cup_groups.csv
│   ├──countries_in_worldcup_18-22.csv
│   ├── gdp.csv
│   ├── ...
│   ├── world_cup_matches.csv
│   ├── world_cups.csv
├── ECE143_presentation_group1.pdf
├── README.md
├── player_data.ipynb               # player data cleaning
├── process_data.py                 # run this file will clean and save cleaned file in .csv
└── visualization.ipynb             # including all the code to generate plots for presentation
```

```
Analysis and Visulization
- The number of times of each country that joins the world cup since 1930
- The number of times of each country that makes it into the Round 16, Quarter-finals, Semi-finals, finals
- The number of goals of each country
- The times of winining and losing in each stage. 
- The trend of wining and losing v.s. GDP for some selected country . 
- The trend of each country’s ranking since 1930 (Might need more data from FIFA or kaggle)
- The population of some countries v.s. their winning rate
- Each countries’ national team players total wages v.s. Their winning rate
- Analysis of 2022 world champion Argentina’s match games (The statistical number when Argentina meets high ranking teams v.s. lower ranking teams)
```

## Third party modules used for data cleaning and data visualization
- numpy 
- pandas
- matplotlib
- seaborn
- plotly


## Data regarding correlation:
- Scatter plot
- Histogram (marginal histogram)
- Correllogram 
https://www.python-graph-gallery.com/

## Contributors
#### Data Acquistion/Cleaning
- Jean Gorby Calicdan
- Zhongkang Fang
#### Data Analysis
- Yiting Shi 
- Zhen Wang
- Puhung Li




