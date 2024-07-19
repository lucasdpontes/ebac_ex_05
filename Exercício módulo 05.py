Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Uso do input e conversão em float (para aceitar todos os números reais)
... x = float(input('Insira um número: '))
... y = float(input('Insira outro número: '))
... 
... operacao = int(input('\nQual operação deseja realizar?\nDigite 1 para soma\nDigite 2 para subtração\nDigite 3 para divisão\nDigite 4 para multiplicação\n'))
... 
... # Implementação de 04 operações, condicional e uso de print
... if operacao == 1:
...   print(x+y)
... elif operacao == 2:
...   print(x - y)
... elif operacao == 3:
...   print(x/y)
... else:
