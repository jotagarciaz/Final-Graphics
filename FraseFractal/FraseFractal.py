import tkinter as tk
from tkinter import ttk, Canvas, Button
from PIL import Image, ImageDraw, ImageTk
import random

from tkcolorpicker import askcolor


CANVAS_HEIGHT = 700
CANVAS_WIDTH = 1000

class GUIProyectoFinal(ttk.Frame):
    
    def __init__(self, main_window):
        self.lineas= []
        self.colors=[]
        self.n_colores=0

        super().__init__(main_window)
        main_window.title("Proyecto Final")
        main_window.geometry('1000x700-150-30')
        
        self.c = Canvas(main_window, bg = "white", height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
        self.c.grid(column=0, row=1)

        self.labelFrame = tk.LabelFrame(main_window)
        self.labelFrame.grid(column=0, row=0, sticky="w")

        self.txtPalabra=tk.Label(self.labelFrame, text="Palabra : ")
        self.txtPalabra.grid(column=0, row=0, padx=5, pady=5)

        self.palabra = tk.StringVar()
        self.entryPalabra = tk.Entry(self.labelFrame, width=10, justify=tk.RIGHT, textvariable=self.palabra)
        self.entryPalabra.grid(column=2, row=0, padx=5, pady=5)

        self.dibujar = Button(self.labelFrame, text="Dibujar", width=8, height=1, command=self.pinta)
        self.dibujar.grid(column=5, row=0, padx=5, pady=5)

        self.longLetra = 15

        #self.labelF = tk.LabelFrame(main_window)
        #self.labelF.grid(column=4, row=0, sticky="w")

        self.txtNColor =  tk.Label(self.labelFrame,text="número de colores: ")
        self.txtNColor.grid(column=3, row=0,padx=5,pady=5)

        
        self.NColores = tk.IntVar()
        self.NColores.set(1)
        self.entryNColores = tk.Entry(self.labelFrame, width=10, justify=tk.RIGHT, textvariable=self.NColores)
        self.entryNColores.grid(column=4, row=0, padx=5, pady=5)



        self.matrizEliminar = [
            [6, 7, 8, 9, 10, 11, 12, 13, 14],  # A
            [7, 8, 9, 10, 11, 12, 13, 14],  # B
            [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14],  # C
            [5, 7, 8, 9, 10, 11, 12, 13, 14],  # D
            [3, 4, 7, 8, 9, 10, 11, 12, 13, 14],  # E
            [3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14],  # F
            [3, 7, 8, 9, 10, 11, 12, 13, 14],  # G
            [2, 6, 7, 8, 9, 10, 11, 12, 13, 14],  # H
            [0, 1, 3, 4, 5, 9, 10, 11, 12, 13, 14],  # I
            [0, 1, 2, 5, 7, 8, 9, 10, 11, 12, 13, 14],  # J
            [2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14],  # K
            [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14],  # L
            [5, 6, 8, 9, 10, 11, 12, 13, 14],  # M
            [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],  # N
            [5, 7, 8, 9, 10, 11, 12, 13, 14],  # O
            [4, 6, 7, 8, 9, 10, 11, 12, 13, 14],  # P
            [5, 7, 8, 10, 11, 12, 13, 14],  # Q
            [4, 6, 7, 8, 10, 11, 12, 13, 14],  # R
            [1, 3, 7, 8, 9, 10, 11, 12, 13, 14],  # S
            [0, 1, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14],  # T
            [2, 5, 7, 8, 9, 10, 11, 12, 13, 14],  # U
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],  # V
            [2, 5, 7, 9, 10, 11, 12, 13, 14],  # W
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14],  # X
            [1, 2, 4, 6, 7, 9, 10, 11, 12, 13, 14],  # Y
            [0, 1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14],  # Z
        ]



    def convertTo(self, mat, pos, letra):
        ascii = ord(letra)
        if ascii > 64:
            index = ascii - 65
            f = self.matrizEliminar[index]
            fila = f[:]
            fila.reverse()
            for f in fila:
                mat.__delitem__(f + pos)

    def ajustarMatriz(self, texto):
        self.n_colores = len(texto) if self.NColores.get() > len(texto) or self.NColores.get()<=0 else self.NColores.get()
        l = len(texto)
        if l == 4:
            self.fractal4()
        elif l == 5:
            self.fractal5()
        elif l == 6:
            self.fractal6()
        elif l == 7:
            self.fractal7()

        index = self.longLetra * (l-1)
        texto.reverse()
        for t in texto:
            self.convertTo(self.lineas, index, t)
            index -= self.longLetra


    def pinta(self):
        for i in range(self.NColores.get()):
            self.colors.append(askcolor((255, 255, 0), self.c)[0])
        texto = list(self.palabra.get().upper())
        self.ajustarMatriz(texto)
        self.pintaIFS()


    def fractal4(self):
        self.lineas = []
        for i in range(4):
            self.generafractal4(self.lineas, i)

    def generafractal4(self, mat, index):
        v = index * 8.3
        lineas = [[0, 0.1, -0.12, 0, -6.8 + v, 7.7],  # Izquierda Arriba
                  [0, 0.1, -0.12, 0, -6.8 + v, 3.4],  # Izquierda Abajo
                  [0.15, 0, 0, 0.07, -4.8 + v, 8.3],  # Arriba
                  [0, 0.1, -0.12, 0, -1.1 + v, 7.7],  # Derecha Arriba
                  [0, 0.1, -0.12, 0, -1.1 + v, 3.4],  # Derecha Abajo
                  [0.15, 0, 0, 0.07, -4.8 + v, 4.4],  # Centro
                  [0.15, 0, 0, 0.07, -4.8 + v, 0.3],  # Abajo
                  [0, 0.1, -0.1, 0, -4 + v, 7.7],  # Linea de arriba hacia el centro (por ejemplo para la M)
                  [0, 0.1, -0.1, 0, -4 + v, 3.1],  # Linea de abajo hacie el centro (por ejemplo para la W)
                  [+0.15, 0.00, -0.08, 0.1, -5 + v, 2.6],  # Palito de R
                  [+0.15, 0.00, 0.1, 0.1, -5 + v, 4.6],  # Palito arriba de la K
                  [+0.15, 0.00, -0.24, 0.1, -5 + v, 6.1],  # Palito de N
                  [+0.18, 0.00, 0.24, 0.1, -5 + v, 1.9],  # Palito inverso de N para X
                  [+0.13, 0.00, -0.23, 0.1, -6.5 + v, 6.3],  # V izquierda
                  [+0.13, 0.00, 0.245, 0.1, -3 + v, 1.9],  # V derecha
                  ]

        for l in lineas:
            mat.append(l)

    def fractal5(self):
        self.lineas = []
        for i in range(5):
            self.generafractal5(self.lineas, i)


    def generafractal5(self, mat, index):
        v = index * 8.3
        lineas = [[0, 0.15, -0.1, 0, -6.8+ v, 7.7],  # Izquierda Arriba
                  [0, 0.15, -0.1, 0, -6.8+ v, 3.0],  # Izquierda Abajo
                  [0.15, 0, 0, 0.06, -5.2+ v, 7.9],  # Arriba
                  [0, 0.15, -0.1, 0, -1.1+ v, 7.7],  # Derecha Arriba
                  [0, 0.15, -0.1, 0, -1.1+ v, 3.0],  # Derecha Abajo
                  [0.15, 0, 0, 0.06, -5.2+ v, 3.8],  # Centro
                  [0.15, 0, 0, 0.06, -5.2+ v, -0.4],  # Abajo
                  [0, 0.1, -0.1, 0, -4+ v, 7.7],  # Linea de arriba hacia el centro (por ejemplo para la M)
                  [0, 0.1, -0.1, 0, -4+ v, 3.1],  # Linea de abajo hacie el centro (por ejemplo para la W)
                  [+0.15, 0.00, -0.1, 0.1, -5+ v, 2.6],  # Palito de R
                  [+0.15, 0.00, 0.09, 0.1, -5+ v, 4.6],  # Palito arriba de la K
                  [+0.15, 0.00, -0.2, 0.1, -5+ v, 6.1],  # Palito de N
                  [+0.18, 0.00, 0.20, 0.1, -5+ v, 1],  # Palito inverso de N para X
                  [+0.1, 0.08, -0.2, 0.05, -6.5 + v, 6.7],  # V izquierda
                  [+0.1, -0.08, 0.22, 0.05, -3 + v, 1],  # V derecha
                  ]

        for l in lineas:
            mat.append(l)

    def fractal6(self):
        self.lineas = []
        for i in range(6):
            self.generafractal6(self.lineas, i)

    def generafractal6(self, mat, index):
        v = index * 8.3
        if index> 0:
            v += 1 * index
        lineas = [[0, 0.1, -0.1, 0, -6.8+ v, 7.7],  # Izquierda Arriba
                  [0, 0.1, -0.1, 0, -6.8+ v, 2],  # Izquierda Abajo
                  [0.11, 0, 0, 0.07, -5+ v, 8.7],  # Arriba
                  [0, 0.1, -0.1, 0, 0+ v, 7.7],  # Derecha Arriba
                  [0, 0.1, -0.1, 0, 0+ v, 2],  # Derecha Abajo
                  [0.11, 0, 0, 0.07, -5+ v, 2.6],  # Centro
                  [0.11, 0, 0, 0.07, -5+ v, -2.5],  # Abajo
                  [0, 0.1, -0.1, 0, -3.9+ v, 7.7],  # Linea de arriba hacia el centro (por ejemplo para la M)
                  [0, 0.1, -0.1, 0, -3.9+ v, 3.1],  # Linea de abajo hacie el centro (por ejemplo para la W)
                  [+0.11, 0.00, -0.08, 0.1, -5+ v, 1.3],  # Palito de R
                  [+0.11, 0.00, 0.08, 0.1, -5+ v, 3.9],  # Palito arriba de la K
                  [+0.11, 0.00, -0.2, 0.1, -5+ v, 7.05],  # Palito de N
                  [+0.11, 0.00, 0.2, 0.1, -5+ v, -1.1],  # Palito inverso de N para X
                  [+0.08, 0.1, -0.18, 0.1, -6.5 + v, 7.05],  # V izquierda
                  [+0.08, -0.1, 0.20, 0.1, -3 + v, -1.5],  # V derecha
                  ]

        for l in lineas:
            mat.append(l)


    def fractal7(self):
        
        self.lineas = []
        for i in range(7):
            self.generafractal7(self.lineas, i)


    def generafractal7(self, mat, index):
        
        v = index * 8.3
        if index> 0:
            v += 7 * index
        lineas = [[0, 0.1, -0.04, 0, -6.8+ v, 7.8],  # Izquierda Arriba
                  [0, 0.1, -0.04, 0, -6.8+ v, 3],  # Izquierda Abajo
                  [0.11, 0, 0, 0.05, -5+ v, 8.3],  # Arriba
                  [0, 0.1, -0.04, 0, 6+ v, 7.8],  # Derecha Arriba
                  [0, 0.1, -0.04, 0, 6+ v, 3],  # Derecha Abajo
                  [0.11, 0, 0, 0.05, -5+ v, 3.3],  # Centro
                  [0.11, 0, 0, 0.05, -5+ v, -1],  # Abajo
                  [0, 0.1, -0.04, 0, -2.1+ v, 7.8],  # Linea de arriba hacia el centro (por ejemplo para la M)
                  [0, 0.1, -0.04, 0, -2.1+ v, 3],  # Linea de abajo hacie el centro (por ejemplo para la W)
                  [+0.11, 0.00, -0.03, 0.1, -5+ v, 2.1],  # Palito de R
                  [+0.11, 0.00, 0.04, 0.1, -5+ v, 3.6],  # Palito arriba de la K
                  [+0.11, 0.00, -0.08, 0.1, -5+ v, 7.05],  # Palito de N
                  [+0.11, 0.00, 0.08, 0.1, -5+ v, -0.2],  # Palito inverso de N para X
                  [+0.05, 0.18, -0.08, 0.11, -6.5 + v, 7.05],  # V izquierda
                  [+0.05, -0.18, 0.08, 0.11, -0.5 + v, -0.2],  # V derecha
                  ]

        for l in lineas:
            mat.append(l)



    def pintaIFS(self):

        mat = self.lineas
        l = len(mat)
        p = 1 / l
        color = int(255/l)
        px, py = 0, 0

        x = px * mat[0][0] + py * mat[0][1] + mat[0][4]
        y = px * mat[0][2] + py * mat[0][3] + mat[0][5]

        WIDTH = 512
        HEIGTH = 512

        xmin = x
        xmax = x
        ymin = y
        ymax = y

        for _ in range (WIDTH * HEIGTH):
            rand = random.random()
            sum = 0
            index = -1
            while (sum < rand):
                sum += p
                index += 1
            nx = x * mat[index][0] + y * mat[index][1] + mat[index][4]
            ny = x * mat[index][2] + y * mat[index][3] + mat[index][5]
            x = nx
            y = ny

            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            if y > ymax:
                ymax = y

        im = Image.new('RGBA', (WIDTH, HEIGTH), (0, 0, 0))
        draw = ImageDraw.Draw(im)

        for i in range (100000):
            rand = random.random()
            sum = 0
            index = -1
            while (sum < rand):
                sum += p
                index += 1
            nx = x * mat[index][0] + y * mat[index][1] + mat[index][4]
            ny = x * mat[index][2] + y * mat[index][3] + mat[index][5]
            x = nx
            y = ny

            nx = int((x - xmin) / (xmax - xmin) * (WIDTH - 1))
            ny = (HEIGTH - 1) - int((y - ymin) / (ymax - ymin) * (HEIGTH - 1))
            if nx < (WIDTH-1) and ny < (HEIGTH-1) and WIDTH >0 and HEIGTH >0:
                
                im.putpixel((int(nx), int(ny)), 255)

                draw.point([int(nx), int(ny)], self.colors[index % self.n_colores])
              

        self.imagen = ImageTk.PhotoImage(im)
        self.c.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=self.imagen)
        self.c.update()


        

main_window = tk.Tk()
app = GUIProyectoFinal(main_window)
app.mainloop()