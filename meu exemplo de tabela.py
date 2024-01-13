
#qtdlinhas = input("digite a quantidade de linhas:")
#qtdcoluna = input("digite a quantidade de colunas:")
#tamcelula = input("digite o tamanho da celula:")

qtdlinhas = 8
qtdcoluna = 4

celula = "___"

coluna=f'|{celula}|'

if int(qtdcoluna) <= 1:
  print()
  for somenteL in range(int(qtdlinhas)):
    print(coluna,end='') 
    print() 
else:
  for somenteL in range(int(qtdlinhas)):
    for somenteC in range(int(qtdcoluna)):
       print(coluna,end='')
    print()