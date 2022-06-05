codigo_compra = input("Digite o codigo de compra: ")
codigo_compra = float(codigo_compra)

if codigo_compra == 5222:
   print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("codigo não cadastrado")