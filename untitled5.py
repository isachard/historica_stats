#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:19:02 2020

@author: Isachard Rodriguez
"""

import pandas as pd
import glob as gl

df = pd.read_csv('mlb/datasets/atlanta.csv')
df.columns = ['Date', 'Team', 'Result', 'Score', 'PitcherF', 'PitcherL',
              'Pitcher H', 'Opponent PitcherF', 'Opponent PitcherL',
              'Opponent Pitcher H', 'Result Run Line', 'Run Line Value',
              'ResultTotal', 'Total Line', 'Total Value']

# print(df.to_string())





print('all csv files in data directory:', gl.glob('mlb/datasets/*.csv'))
for filename in gl.glob('mlb/datasets/*.csv'):
    data = pd.read_csv(filename)
    data.columns = ['Date', 'Team', 'Result', 'Score', 'PitcherF', 'PitcherL',
                    'Pitcher H', 'Opponent PitcherF', 'Opponent PitcherL',
                    'Opponent Pitcher H', 'Result Run Line', 'Run Line Value',
                    'ResultTotal', 'Total Line', 'Total Value']
    print(filename[13:-4])
    #print(data['ResultTotal'].value_counts())
    #print(data['ResultTotal'].value_counts().plot(kind='bar'))
    over = data.loc[data.ResultTotal == 'O', 'ResultTotal'].count()
    under = data.loc[data.ResultTotal == 'U', 'ResultTotal'].count()
    total_over_perc = round((over / (over + under)) *100,2)
    total_under_perc = round((under / (over + under)) *100,2)
    

        
    print( "Over: " + str(total_over_perc))
    print("Under: " + str(total_under_perc))
    print()

