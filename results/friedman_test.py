import pandas as pd
from scipy.stats import friedmanchisquare

files = ['Ranks_2D.csv', 'Ranks_10D.csv', 'Ranks_30D.csv']

for file in files:
    data = pd.read_csv(file)
    statistic, p_value = friedmanchisquare(data['DE_rand_1_bin'], data['DE_best_1_bin'], data['PSO'], data['SOMA_all_to_one'], data['SOMA_all_to_all'])

    print('----------------------------------------------------------')
    print(file)
    print(f'Friedman Test Statistic: {statistic}')
    print(f'P-value: {p_value}')

