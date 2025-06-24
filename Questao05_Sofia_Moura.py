import turtle as t

t.pensize(2)

base=150 # Largura do triângulo
altura=120 # Altura do triângulo
espaco=30 # Espaço entre os triângulos

# Posição inicial das coordenadas
inicio_x = -300
inicio_y = 300
t.penup()
# Canto superior esquerdo do triângulo vermelho 
t.goto(inicio_x, inicio_y) 
t.pendown()

# Desenho do triangulo vermelho
t.fillcolor('red')
t.begin_fill()
t.goto(inicio_x+base,inicio_y) # Canto superior direito
t.goto(inicio_x+base/2,inicio_y-altura) # Canto inferior
t.goto(inicio_x, inicio_y) # Canto superior
t.end_fill()
#-----------------


# Dado o espaçamento entre os triângulos
# Posição inicial das coordenadas, para iniciar o desenho do triângulo verde
inicio_x +=( base + espaco)
t.penup()
t.goto(inicio_x, inicio_y)
t.pendown()

#Desenho triangulo verde
t.fillcolor('green')
t.begin_fill()
t.goto(inicio_x+base/2, inicio_y-altura) # Canto inferior direito
t.goto(inicio_x-base/2,inicio_y-altura) # Canto inferior esquerdo
t.goto(inicio_x, inicio_y) # Canto superior
t.end_fill()
#-----------------

# Dado o espaçamento entre os triângulos
# Posição inicial das coordenadas, para iniciar o desenho do triângulo azul
inicio_x += espaco
t.penup()
t.goto(inicio_x, inicio_y)
t.pendown()

#Desenho do triangulo azul
t.fillcolor('blue')
t.begin_fill()
t.goto(inicio_x+base,inicio_y)
t.goto(inicio_x+base/2,inicio_y-altura)
t.goto(inicio_x, inicio_y)
t.end_fill()
#-----------------

t.mainloop()
