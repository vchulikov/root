import pandas as pd
pd.read_csv('all_data.csv', header=None).T.to_csv('all_data_transpose.csv', header=False, index=False)
