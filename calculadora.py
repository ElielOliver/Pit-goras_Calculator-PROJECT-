import math

cat1 = input('Digite o valor do primeiro cateto em cm (caso não tenha, digite "X") ')
cat2 = input('Digite o valor do segundo cateto em cm (caso não tenha, digite "X") ')
hip = input('Digite o valor da hipotenusa (caso não tenha, digite "X") ')
try:
    if cat1 != '' and cat2 != '' and hip != '':
        if cat1.upper() == 'X' and cat2.upper() != 'X' and hip.upper() != 'X':
            cat2 = float(cat2)
            hip = float(hip)
            cat = math.sqrt((hip ** 2) - (cat2 ** 2))
            print(f'O valor do cateto é {cat:.2} cm.')
        elif cat2.upper() == 'X' and cat1.upper() != 'X' and hip.upper() != 'X':
            cat1 = float(cat1)
            hip = float(hip)
            cat = math.sqrt((hip ** 2) - (cat1 ** 2))
            print(f'O valor do cateto é {cat:.2} cm.')
        elif hip.upper() == 'X' and cat2.upper() != 'X' and cat1.upper() != 'X':
            cat1 = float(cat1)
            cat2 = float(cat2) 
            hipo = math.sqrt((cat1 ** 2) + (cat2 ** 2))
            print(f'O valor da hipotenusa é {hipo:.2} cm.')
        else:
            print('ERROR: Digite a incógnita corretamente!')
    else:
        print('Digite os  valores corretamente!')
except ValueError:
    print('Erro de formatação! Digite os valores corretamente!')