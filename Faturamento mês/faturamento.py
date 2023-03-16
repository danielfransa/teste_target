import io
import json

with io.open('D:/workspace/EstudosPython/Test_Target/dados/dados.json', 'r', encoding = 'utf-8') as json_file:
    datas = json.load(json_file)

soma = 0
maior = -99999.99
menor = 99999.99
dia_maior = ""
dia_menor = ""
count = 0
dias_zero = 0

for data in datas:
    valor = data.get('valor')
    soma = soma + valor
    count = count + 1

    if valor > maior:
        maior = valor
        dia_maior = data.get('dia')
    
    if valor == 0:
        dias_zero = dias_zero + 1
    elif valor < menor:
        menor = valor
        dia_menor = data.get('dia')
        


media_diaria = soma / (count - dias_zero)

count = 0
dias_com_faturamento_acima_media=[]
for data in datas:
    valor = data.get('valor')
    if valor > media_diaria:
        count = count + 1
        dias_com_faturamento_acima_media.append(data.get('dia'))



print("Faturamento Mensal: ", soma)
print("Dia de maior venda: ", dia_maior, "Valor: ", maior)
print("Dia de menor venda: ", dia_menor, "Valor: ",  menor)
print("Numero de dias no mes em que o faturamento diario foi maior que a media mensal: ", count)
print("Esse dias foram: ",dias_com_faturamento_acima_media)



