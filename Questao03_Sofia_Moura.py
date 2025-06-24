import turtle as t
import random

# Leitura da quantidade de retângulos
n=int(input("Digite a quantidade de retângulos: "))

# Definindo as cores usando a notação RGB
t.colormode(255) 

# Ajustando a posição da caneta, para centralizar o retângulo na tela
t.penup()
t.backward(150)
t.right(90)
t.forward(150)
t.left(90)
t.pendown()

t.pensize(4)

for i in range(n):
    # Gerando cores aleatórias usando a função random.randint
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Desenhando retângulo
    t.fillcolor(r, g, b)
    t.begin_fill()

    t.forward(350)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(35)

    t.end_fill()

    # Espaçamento entre os retângulos
    t.penup()
    t.forward(60)
    t.pendown()
    t.right(90) # Ajustando a posição da caneta

t.mainloop()