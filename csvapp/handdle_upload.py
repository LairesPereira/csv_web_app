import pandas as pd

user_file = []
css_class = 'comicGreen'

test_file = {
        'myfile': '/Users/Dev/Documents/10_nubank_outubro_2023.csv'
}

pd.set_option('display.max_rows', None)

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
        transaction_type = user_file_copy['Descrição'].str.split('-').str[0]

        # handle chargeback cases that contain an extra "-"
        if transaction_type.str.contains('estorno').any():
                reversal_index = user_file_copy.loc[user_file_copy['Descrição'].str.contains('estorno', na=False)].index.tolist() # find all chargebacks indexes
                reversal_transactions = user_file_copy.loc[reversal_index] # create a df with chargebacks only
                reversal_transactions['Descrição'] = reversal_transactions['Descrição'].str.replace(r'-.+?-', '-', regex=True) # deletes problematic descriptions
                user_file_copy.update(reversal_transactions, overwrite=True) # updates out main df with regex corrections
                
        transaction_owner =  user_file_copy['Descrição'].str.split('-').str[1]
        
        df = user_file_copy.drop('Descrição', axis='columns')
        df.insert(1, 'Tipo', transaction_type)
        df.insert(2, 'Titular', transaction_owner)
        df = df.fillna('') # Replace all NaN 

        mask = df['Titular'].str.contains(name)
        new = df.loc[mask]
        print(new)
        if new.empty:
                return 'empty'
        return new.to_html(classes=css_class)


handle_uploaded_file(test_file)
read_strict('laires')