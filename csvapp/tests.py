import pandas as pd

# IMPORTANT
# Always create and use a copy of original df stored in user_file

user_file = []
css_class = 'comicGreen'

# Creates the df that will be copied by other methods
def handle_uploaded_file(): 
        df = pd.read_csv('/Users/Dev/Documents/10_nubank_outubro_2023.csv').drop('Identificador', axis='columns').reindex(columns=['Data', 'Descrição', 'Valor'])
        df['Descrição'] = df['Descrição'].apply(lambda x: x.lower() if isinstance(x, str) else x) # transform all itens in description to lower case
        user_file.append(df)

# returns a new df with only the rows that match string "name"
def read_strict(name):
        user_file_copy = user_file[0]
        mask = user_file_copy['Descrição'].str.contains(name)
        new = user_file_copy.loc[mask]
        return new

# returns how many times a name appears in df
def matches(name):
        user_file_copy = user_file[0]
        times = user_file_copy['Descrição'].to_string().lower().count(name) 
        return times

        
handle_uploaded_file()
read_strict('laires')
