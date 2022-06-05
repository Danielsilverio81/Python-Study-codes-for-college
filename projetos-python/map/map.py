# Exemplo
print("Exemplo")
linguagens = '''python java javascript c c# c++ swift go Kotlin''' .split()

nova_lista = map(lambda x: x.upper(), linguagens)
print(f"A nova lista é = {nova_lista}\n")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")