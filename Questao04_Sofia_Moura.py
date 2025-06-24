import turtle as t

# Leitura da quantidade de triângulos
n = int(input("Digite a quantidade de triângulos: "))

W = 700 # largura da imagem 
l = 50 # lado do triângulo

s = W // (n + 1) # Dimensão dos segmentos
espaco_entre = (s - l) # Comprimento da linha conectando dois triângulos
espaco_in_fim =  s - (l// 2) # Espaço antes do primeiro triângulo e depois do último triângulo 

t.pensize(4)

# Posiciona a caneta na coordenada indicada
t.penup()
t.goto(-W/2, 0)
t.pendown()


for i in range(n):
    # Caso seja o início da imagem adiciona o espaço s-l/2
    if i == 0: 
        t.forward(espaco_in_fim)
    else: # Caso contrário adiciona s-l (espaço que conecta dois triângulos)
        t.forward(espaco_entre)

    # Desenha o triângulo
    t.left(60)
    t.forward(l)
    t.right(120)
    t.forward(l)
    t.left(60)

    # Caso esteja no ultimo triângulo a ser desenhado
    # Adiciona o espaço depois do último triângulo que será s – l/2.
    if i == n - 1:
        t.forward(espaco_in_fim)


t.mainloop()
