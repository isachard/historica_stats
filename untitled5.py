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
              'Result Total', 'Total Line', 'Total Value']

# print(df.to_string())
print('all csv files in data directory:', gl.glob('mlb/datasets/*.csv'))
for filename in gl.glob('mlb/datasets/*.csv'):
    data = pd.read_csv(filename)
    data.columns = ['Date', 'Team', 'Result', 'Score', 'PitcherF', 'PitcherL',
                    'Pitcher H', 'Opponent PitcherF', 'Opponent PitcherL',
                    'Opponent Pitcher H', 'Result Run Line', 'Run Line Value',
                    'Result Total', 'Total Line', 'Total Value']
    print(filename[13:-4])
    print(data['Result Total'].value_counts())
    print(data['Result Total'].value_counts().plot(kind='bar'))