import tkinter as tk

# Criação da janela
window = tk.Tk()
window.geometry("800x600")
canvas = tk.Canvas(window, width=800, height=600)

base=150 # Largura do triângulo
altura=120 # Altura do triângulo
espaco=30 # Espaço entre os triângulos


#Desenho triângulo vermelho
# Coordenadas do início do desenho
inicio_x = 200
inicio_y =200

canvas.create_polygon(
    [
        inicio_x, inicio_y, # Canto superior esquerdo
        inicio_x + base, inicio_y, # Canto superior direito
        inicio_x + base/2, inicio_y + altura, # Canto inferior
        inicio_x, inicio_y  # volta ao ponto inicial
    ],
    outline='black', fill='red')

#Desenho triângulo verde
# Coordenadas do início do desenho
# Iniciando o desenho no canto inferior esquerdo
inicio_x +=((base//2)+espaco)
inicio_y += altura

canvas.create_polygon(
    [
        inicio_x, inicio_y, # Canto inferior esquerdo
        inicio_x + base, inicio_y, # Canto inferior direito
        inicio_x + base/2, inicio_y - altura,  # Canto superior
        inicio_x, inicio_y  
    ],
    outline='black', fill='green')

#Desenho triângulo azul
# Coordenadas do início do desenho
inicio_x = 200+ base + 2*espaco
inicio_y =200

canvas.create_polygon(
    [
        inicio_x, inicio_y,  # canto superior esquerdo 
        inicio_x + base, inicio_y,  # canto superior direito 
        inicio_x + base/2, inicio_y + altura,  # vértice inferior 
        inicio_x, inicio_y  
    ],
    outline='black', fill='blue')

canvas.pack() 
window.mainloop()