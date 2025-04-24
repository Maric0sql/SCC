print('Average exchange rate of foreign currencies')

print('Enter the amount you want to convert')
valor = float(input('(use . instead of ,): '))

euro = 6.20
dolar_ame = 5.83
libra_est =  7.43

print('Which currency do you want to convert the Brazilian Real to?')
print('1- to Euro')
print('2- to US Dollar')
print('3- to British Pound')

escolha = int(input('Enter your option: '))

if escolha == 1:
    print(f'Your value in Euro will be approximately: ' + str(valor/euro))

elif escolha == 2:
    print(f'Your value in US Dollar will be approximately: ' + str(valor/dolar_ame))

if escolha == 3:
    print(f'Your value in British Pounds will be approximately: ' + str(valor/libra_est))
