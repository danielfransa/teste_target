dic = {'SP': 67836.43, 'RJ' : 36678.66, 'MG' : 29229.88, 'ES' : 27165.48, 'Outros' : 19849.53}

soma_total_vendas = 0

for valor in dic.values():
    soma_total_vendas = soma_total_vendas + valor

porcentagem = 0.0
lista=[]
dic_porcentagem = dic.keys()

for valor in dic.values():
    porcentagem = (valor * 100) / soma_total_vendas
    lista.append('{0:.2f}'.format(porcentagem))

dic_porcentagem = dict(zip(dic_porcentagem, lista))

print(dic_porcentagem)





