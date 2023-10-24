import pandas as pd
import csv

def handle_uploaded_file(file): 
        file_info = pd.read_csv(file['myfile'])
        # final_extraction = []
        # for index, row in file_info.iterrows():
        #         transaction_info = {
        #             "name": row['Descrição'],
        #             "value": row['Valor'],
        #         }
        #         final_extraction.append(transaction_info)
        #         print(row['Descrição'], row['Valor'])
        return file_info.to_html()
               





# def getTransactionsInfo(file):
#     with open('csv_files/' + file, 'r') as csvfile:
#         csv_reader = csv.DictReader(csvfile, delimiter=',')
#         final_list = []
#         for line in csv_reader:
#             if('Boleto' in line['Descrição']): continue
#             elif('fatura' in line['Descrição']): continue
#             elif('recarga') in line['Descrição'].lower(): continue
#             else:
#                 transaction_info = {
#                     "date": line['Data'],
#                     "type": line['Descrição'].split('-')[0].lower(),
#                     "name": line['Descrição'].split('-')[1].lower(),
#                     "value": line['Valor'],
#                 }
#                 final_list.append(transaction_info)    
#         return final_list


