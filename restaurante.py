class Restaurante: 
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praca'
# Passo 1
restaurante_praca.categoria = 'Italiana'

# Passo 2 e 3
print(f' - O restaurante {restaurante_praca.nome}  esta ativo' if restaurante_praca.ativo else f' O restaurante {restaurante_praca.nome} esta inativo')

# Passo 4 
categoria = restaurante_praca.nome
print(f'A categoria do restaurante eh: {categoria}')

# Passo 5 
restaurante_praca.nome = 'Bistro'
print(vars(restaurante_praca))

#Passo 6
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

print(f'A categoria do {restaurante_pizza.nome} eh Fast Food' if restaurante_pizza.categoria == 'Fast Food' else 'A categoia do {restaurante_pizza.nome} nao eh Fast Food')