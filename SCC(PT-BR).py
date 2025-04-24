print('Média de cotação de moedas extrangeiras')

print('Digite o valor que você deseja converter')
valor = float(input('(coloque o valor com . ao invés de ,): '))

euro = 6.20
dolar_ame = 5.83
libra_est =  7.43

print('Qual moeda deseja converter o Real Brasileiro?')
print('1- para Euro')
print('2- para Dólar Americano')
print('3- para Libra Esterlina')

escolha = int(input('Digite a opção: '))

if escolha == 1:
    print(f'Seu valor em Euro será aproximadamente: ' + str(valor/euro))

elif escolha == 2:
    print(f'Seu valor em Dólar Americano será aproximadamente: ' + str(valor/dolar_ame))

if escolha == 3:
    print(f'Seu valor em Libras Esterlinas será aproximadamente: ' + str(valor/libra_est))