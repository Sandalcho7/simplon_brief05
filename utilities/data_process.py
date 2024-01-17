import pandas as pd

# Path for csv files
main_csv = r'\\wsl.localhost\Ubuntu\home\sandalcho7\prairie\simplon_brief05\ressources\data\transactions.csv'

# Main dataframe creation
df = pd.read_csv(main_csv)

# Creating a dataframe copy for a restricted area (around Paris) and transactions in 2022
paris_df = df[(df.departement.isin([75, 77, 78, 91, 92, 93, 94, 95])) & (df.date_transaction.str.startswith('2022-'))].copy()


# Data cleaning/processing
paris_df = paris_df.drop('Unnamed: 0', axis=1)   # dropping useless column
paris_df = pd.get_dummies(paris_df, columns=['type_batiment'], dtype=int, prefix='type')   # processing 'type_batiment' into numerical values

paris_df['date_transaction'] = pd.to_datetime(paris_df['date_transaction'])   # processing 'transaction_date' into numerical values
reference_date = pd.to_datetime('1970-01-01')
paris_df['days_since_epoch'] = (paris_df['date_transaction'] - reference_date).dt.days
paris_df = paris_df.drop('date_transaction', axis=1)

surface_cols = [c for c in df.columns if 'surface_' in c and c != 'surface_habitable']   # cleaning dataframe from transactions with farmland, commercial spaces, etc.
for c in surface_cols:
    paris_df[c + '_sum'] = paris_df[c].apply(lambda x: sum(eval(x)) if 'NULL' not in x else 0)
    
paris_df = paris_df[paris_df[[c + '_sum' for c in surface_cols]].sum(axis=1) == 0]

paris_df['prix_m2'] = paris_df['prix'] / paris_df['surface_habitable']   # adding a 'prix_m2' column


# Exporting the dataframe as a csv
export_path = r'\\wsl.localhost\Ubuntu\home\sandalcho7\prairie\simplon_brief05\ressources\data\paris_df.csv'

paris_df.to_csv(export_path, index=False)