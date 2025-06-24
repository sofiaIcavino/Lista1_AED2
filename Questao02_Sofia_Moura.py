import turtle as t

# Definindo as cores usando a notação RGB
t.colormode(255) 

# Andando para trás, para centralizar o retângulo na tela
t.penup()
t.backward(150)
t.pendown()

t.pensize(4) # Definindo a grossura do traço da caneta

# Desenho retângulo verde
t.fillcolor(164,223,164) # Cor verde
t.begin_fill()

t.forward(350)
t.right(90) # Curva 90° à direita
t.forward(35)
t.right(90)
t.forward(350)
t.right(90)
t.forward(35)

t.end_fill()

# Espaçamento entre os dois retângulos
t.penup()
t.forward(60)
t.pendown()

# Desenho retângulo azul
t.fillcolor(164,199,223) # Cor azul
t.begin_fill()

t.right(90)
t.forward(350)
t.right(90)
t.forward(35)
t.right(90)
t.forward(350)
t.right(90)
t.forward(35)

t.end_fill()


t.mainloop()

