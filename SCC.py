print('Average Exchange Rates for Foreign Currencies')

print('Enter the amount you want to convert')
amount = float(input('(use . instead of ,): '))

euro = 6.20
usd = 5.83
gbp = 7.43

print('Which currency would you like to convert the Brazilian Real into?')
print('1 - Euro')
print('2 - US Dollar')
print('3 - British Pound')

choice = int(input('Enter your option: '))

if choice == 1:
    print(f'Your amount in Euros is approximately: {amount / euro:.2f}')

elif choice == 2:
    print(f'Your amount in US Dollars is approximately: {amount / usd:.2f}')

elif choice == 3:
    print(f'Your amount in British Pounds is approximately: {amount / gbp:.2f}')