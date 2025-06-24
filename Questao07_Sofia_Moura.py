import tkinter as tk

# Função para desenhar um círculo nas coordenadas x e y e uma determinada cor
def circulo(x,y,raio,cor):
    canvas.create_oval(x, y, raio+x, raio+y, outline=cor, width=10)

window = tk.Tk()
window.geometry("800x600")
canvas = tk.Canvas(window, width=800, height=600)

# Lista de cores pré-definidas
cores = ['#0885c2', '#fbb132', 'black', '#1c8b3c', '#ed334e']
x,y=70,100 # Definindo as coordenadas x e y

# Desenho dos 5 círculos
for i in range(5):
    if i%2==0: # Desenha os círculos de cima
        circulo(x+(i*100),y,200,cores[i])
    else: # Desenha os círculos de baixo
        circulo(x+(i*100),y+(100),200,cores[i])
    x+=15

canvas.pack() 
window.mainloop()