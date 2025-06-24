import tkinter as tk

#Leitura do valor T
T=int(input("Informe o valor de T: "))

#Definindo o tamanho da janela de acordo com as regiões de altura e largura T
window = tk.Tk()
canvas = tk.Canvas(window, width=2*T+10, height=2*T+10)
canvas.pack()


canvas.create_line(T, 0, T, 2*T, width=2)   # linha vertical
canvas.create_line(0, T, 2*T, T, width=2)   # linha horizontal


# Desenho: Triangulo
lado_t = 0.9 * T
x = T + T*0.05    # (T*0.05)-> dar um espaçamento para nao ficar grudado na linha
y = T - T*0.05     

canvas.create_polygon(
    [
        x, y, # vértice inferior esquerdo
        x + lado_t, y, # vértice inferior direito
        x + lado_t / 2, y - lado_t  # vértice superior 
    ],
    outline='darkgreen', fill='lightgreen')
#-----------------


# Desenho: Circulo
raio = 0.45 * T
x= T / 2
y= 3 * T / 2  
canvas.create_oval(x-raio, y-raio, raio+x, raio+y, outline='red',fill='pink')
#-----------------


# Desenho: Quadrado
lado_q = 0.9 * T
x = T + T*0.05    # (T*0.05)-> dar um espaçamento para nao ficar grudado na linha
y = T + T*0.05 

canvas.create_polygon(
    [
        x, y,  # vértice superior esquerdo                  
        x + lado_t, y, # vértice superior direito              
        x + lado_t , y + lado_t, # vértice inferior direito
        x, y + lado_t, # vértice inferior esquerdo
        x, y, # volta ao inicio
    ],
    outline='darkblue', fill='lightblue')
#-----------------

canvas.pack() 
window.mainloop()