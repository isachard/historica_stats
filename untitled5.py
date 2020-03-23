#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:19:02 2020

@author: shka
"""

import pandas as pd
df = pd.read_csv("mlb/datasets/miami.csv")
df.columns = ['Date', 'Team', 'Result', 'Score', 'PitcherF','PitcherL', 
              'Pitcher H', 'Opponent PitcherF',' Opponent PitcherL', 
              'Opponent Pitcher H', 'Result Run Line','Run Line Value',
              'Result Total', 'Total Line', 'Total Value']
  


print(df.to_string())
