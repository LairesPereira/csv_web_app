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
def read_strict(urlParams):
        print('url', urlParams)
        final_info = {
                'table': '',
                'total_transactions': 0,
                'transactions_sum': 0 
        }

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

        mask_name = df['Titular'].str.contains(urlParams['name_filter'])

        new = df.loc[mask_name]
        
        transactions_full_sum = new['Valor'].sum()* -1

        final_info['table'] = new.to_html(classes=css_class)
        final_info['total_transactions'] = new.shape[0]
        final_info['transactions_sum'] = round(transactions_full_sum, 2)

        # if user wants only send or recived transactions we do filter new df again
        if urlParams['send_checkbox'] == 'true':
                mask_new_send = new['Tipo'].str.contains('enviada')
                
                new_send = new.loc[mask_new_send]

                transactions_full_sum = new_send['Valor'].sum()

                final_info['table'] = new_send.to_html(classes=css_class)
                final_info['total_transactions'] = new_send.shape[0]
                final_info['transactions_sum'] = round(transactions_full_sum, 2)

         



        # ******DEBUG PRINT - DELETE LATER*****
        # print(new)
        # print('-' * 10)
        # print(new.shape[0])
        # print(round(transactions_full_sum, 2))
        # ******DEBUG PRINT - DELETE LATER*****
        
        if new.empty:
                return 'empty'
        return final_info


handle_uploaded_file(test_file)
read_strict({
                'name_filter': 'laires',
                'send_checkbox': 'true',
                'recived_checkbox': 'true'
        })