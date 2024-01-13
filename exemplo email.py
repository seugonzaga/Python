compra_c = True
dados_c = "compra no valor de 12,50"

for enviar in range(3):
  if compra_c:
    print(dados_c)
    print("detalhes enviados")
    break
  else:
    print("falha na compra")
