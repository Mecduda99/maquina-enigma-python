
# Crie uma lista alphabet contendo todas as letras do alfabeto em inglês em ordem alfabética. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

# Crie uma lista rotor que represente um rotor simples. Para isso, embaralhe as letras do alfabeto de alguma forma. 
rotor = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c'] 

# Crie uma lista reflector que represente um refletor simples. Para isso, embaralhe novamente as letras do alfabeto de outra maneira. 
refletor = [] 
for i in reversed(alphabet): 
    refletor.append(i) 



# Dado um message (mensagem), você deve cifrar a mensagem da seguinte maneira: 
mensagem = input('informe a mensagem que deseja criptografar: ') 
letras_mensagem = list(mensagem) 

# Para cada letra da mensagem, encontre sua posição no alphabet. 
# Adicione 1 à posição encontrada (simulando uma rotação simples) e, em seguida, encontre a letra correspondente no rotor. 
posicao_letras_a = [] 

for i in range(0, len(letras_mensagem)): 
    for j in range(0, len(alphabet)): 
        if letras_mensagem[i] == alphabet[j]: 
            posicao_letras_a.append(j+1)

letras_rotor = []

for i in range(0, len(posicao_letras_a)):
    for j in range(0, len(rotor)):
        if posicao_letras_a[i] == j:
            letras_rotor.append(rotor[j])

# Encontre a posição dessa letra no reflector e encontre a letra correspondente no alphabet. 
posicao_refletor = []

for i in range(0, len(letras_rotor)):
    for j in range(0, len(refletor)):
        if letras_rotor[i] == refletor[j]:
            posicao_refletor.append(j)

letras_cifrada = []

for i in range(0, len(posicao_refletor)):
    for j in range(0, len(alphabet)):
        if posicao_refletor[i] == j:
            letras_cifrada.append(alphabet[j])

# Adicione a letra cifrada à mensagem cifrada. 
mensagem_cifrada = ''.join(letras_cifrada)

# Mostre a mensagem cifrada. 
#  MENSAGEM ENIGMÁTICA - FINAL
print("Sua mensagem criptografada é: " + "'" + mensagem_cifrada + "'")


#  DESCRIPTOGRAFANDO MENSAGEM

# Para decifrar a mensagem cifrada, siga o processo inverso: 
# Para cada letra da mensagem cifrada, encontre sua posição no alphabet. 
letras_mensagem_cifrada = list(mensagem_cifrada)
posicao_letrascifra_a = []
for i in range(0, len(letras_mensagem_cifrada)):
    for j in range(0, len(alphabet)):
        if letras_mensagem_cifrada[i] == alphabet[j]:
            posicao_letrascifra_a.append(j)

# Encontre a posição dessa letra no reflector e encontre a letra correspondente no alphabet. 
posicao_refletor_cifra = []
for i in range(0, len(letras_mensagem_cifrada)):
    for j in range(0, len(refletor)):
        if letras_mensagem_cifrada[i] == refletor[j]:
            posicao_refletor_cifra.append(j)

letras_refletor_cifra_a = []
for i in range(0, len(posicao_refletor_cifra)):
    for j in range(0, len(alphabet)):
        if posicao_refletor_cifra[i] == j:
            letras_refletor_cifra_a.append(alphabet[j])
            
# Encontre a posição dessa letra no rotor e subtraia 1 da posição (simulando a rotação inversa). 
posicao_rotor_cifra = []
for i in range(0, len(letras_refletor_cifra_a)):
    for j in range(0, len(rotor)):
        if letras_refletor_cifra_a[i] == rotor[j]:
            posicao_rotor_cifra.append(j-1)

# Adicione a letra decifrada à mensagem decifrada. 
letras_decifradas = []
for i in range(0, len(posicao_rotor_cifra)):
    for j in range(0, len(alphabet)):
        if posicao_rotor_cifra[i] == j:
            letras_decifradas.append(alphabet[j])

mensagem_decifrada = ''.join(letras_decifradas)
# Mostre a mensagem decifrada. 
print("A mensagem decifrada é: " + "'" + mensagem_decifrada + "'")

