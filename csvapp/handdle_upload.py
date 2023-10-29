import pandas as pd

user_file = []
css_class = 'comicGreen'

# IMPORTANT
# Always create and use a copy of original df stored in user_file
def handle_uploaded_file(file): 
        df = pd.read_csv(file['myfile']).drop('Identificador', axis='columns').reindex(columns=['Data', 'Descrição', 'Valor'])
        df['Descrição'] = df['Descrição'].apply(lambda x: x.lower() if isinstance(x, str) else x) # transform all itens in description to lower case
        user_file.append(df)
        return user_file[0].to_html(classes=css_class)

# returns a new df with only the rows that match string "name"
def read_strict(name):
        user_file_copy = user_file[0]
        mask = user_file_copy['Descrição'].str.contains(name)
        new = user_file_copy.loc[mask]
        return new.to_html(classes=css_class)


