import pandas as pd

# Return all transactions 
def handle_uploaded_file(file): 
        file_info = pd.read_csv(file['myfile']).drop('Identificador', axis='columns').reindex(columns=['Data', 'Descrição', 'Valor'])
        return file_info.to_html()
               