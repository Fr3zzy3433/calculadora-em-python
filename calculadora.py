while True:
   numero_1 = input('Digite um número: ')
   numero_2 = input('Digite um segundo número: ')
   operador = input('Escolha uma ação (+-/*): ')

   numeros_validos = None
   numero_1_float = 0
   numero_2_float = 0
   
   try:
    numero_1_float = float(numero_1)
    numero_2_float = float(numero_2)
    numeros_validos = True

   except:
     numeros_validos = None

   if numeros_validos is None:
        print('Um ou ambos os números são invalidos')
        continue

   operadores_permitdos = '+-/*'

   if operador not in operadores_permitdos:
        print('Invalid operador')
        continue
   if len(operador) > 1:
        print('Digite apenas um operador')

   print('Realizando sua operação')

   if operador == '+':
    print(f'{numero_1_float} + {numero_2_float} = ',numero_1_float + numero_2_float)

   if operador == '-':
    print(f'{numero_1_float} - {numero_2_float} = ',numero_1_float  -numero_2_float)

   if operador == '/':
    print(f'{numero_1_float} / {numero_2_float} = ',numero_1_float / numero_2_float) 

   if operador == '*':
    print(f'{numero_1_float} * {numero_2_float} = ',numero_1_float * numero_2_float)



   sair = input('Deseja sair? [y/n]  ').lower().startswith('y')
   if sair == True:
        break
   else:
    continue