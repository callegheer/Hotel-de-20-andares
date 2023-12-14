# Todos os numeros exceto 13 - ordem crescente - for i in rage
numero = 0
for i in range(20):
  numero = numero + 1
  if (numero == 13):
    continue
  print(numero)
  
# Todos os numeros exceto 13 - ordem decrescente - for i in rage
for i in range(20, 0, -1):
  if ( i == 13):
    continue
  print(i)

# Todos os numeros exceto o 13 - laço while
Contador = 1
while (Contador <= 20):
  if (Contador == 13):
    Contador = Contador + 1
    continue
  else:
    print(Contador)
    Contador = Contador + 1