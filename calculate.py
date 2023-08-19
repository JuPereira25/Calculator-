
"""
Calculadora com While
"""

while True:
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    operation = input('Please type in the math operation you would like to complete (+-/*): ')
               
   
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))  #format permite substitui as chaves pelos valores number1 e number2
        print(number_1 + number_2)
    
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 *  number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('invalid operation')

        sair = input('Quer sair[S]im: ')
        sair = sair.lower() 
        print(sair)     #converte em letras minisculas 
        break
        
