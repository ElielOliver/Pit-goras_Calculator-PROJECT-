cat1 = input('Digite o valor do primeiro cateto em cm (caso não tenha, digite "X") ')
cat2 = input('Digite o valor do segundo cateto em cm (caso não tenha, digite "X") ')
hip = input('Digite o valor da hipotenusa (caso não tenha, digite "X") ')
if cat1 and cat2 and hip:
    if cat1 != '' and cat2 != '' and hip != '':
        if cat1.upper() == 'X' and cat2.upper() != 'X' and hip.upper() != 'X':
            cat2 = cat2.replace(',','.')
            hip = hip.replace(',', '.')
            cat2 = float(cat2)
            hip = float(hip)
            cat = ((hip ** 2) - (cat2 ** 2)) ** (1/2)
            cat = round(cat, 2)
            cat = str(cat)
            print(f'O valor do cateto é {cat.replace('.', ',')} cm.')
        elif cat2.upper() == 'X' and cat1.upper() != 'X' and hip.upper() != 'X':
            cat1 = cat1.replace(',','.')
            hip = hip.replace(',', '.')
            cat1 = float(cat1)
            hip = float(hip)
            cat = ((hip ** 2) - (cat1 ** 2)) ** (1/2)
            cat = round(cat, 2)
            cat = str(cat)
            print(f'O valor do cateto é {cat.replace('.', ',')} cm.')
        elif hip.upper() == 'X' and cat2.upper() != 'X' and cat1.upper() != 'X':
            cat2 = cat2.replace(',','.')
            cat1 = cat1.replace(',', '.')
            cat1 = float(cat1)
            cat2 = float(cat2) 
            hipo = ((cat1 ** 2) + (cat2 ** 2)) ** (1/2)
            hipo = round(hipo, 2)
            hipo = str(hipo)
            print(f'O valor da hipotenusa é {hipo.replace('.', ',')} cm.')
        else:
            print('ERROR: Digite a incógnita corretamente!')
    else:
        print('Digite os  valores corretamente!')
else:
    print('Erro de formatação! Digite os valores corretamente!')