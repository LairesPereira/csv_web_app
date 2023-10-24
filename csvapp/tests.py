nomes = ['monique', 'laires', 'rene']

print(nomes)

def login(lista_logins):
    novo_login = input('Digite seu nome')
    if novo_login in lista_logins:
        print('O usuario ja existe')
    else:
        lista_logins.append(novo_login)
        print('usuario cadastrado')
        print(nomes)
    

print(nomes)

login(nomes)













# nomes = ['laires', 'rene', 'rian']


# def function(names:list):
#     new_user = input('Digite um novo nome')
#     while True:
#         if not new_user in names:
#             names.append(new_user)
#             print(nomes)
#             break
#         else: 
#             print('ja existe')
#             break


# print(nomes)

# function(nomes)