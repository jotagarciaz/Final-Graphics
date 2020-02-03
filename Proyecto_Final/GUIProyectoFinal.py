import tkinter as tk
from tkinter import ttk, Canvas, Button
from PIL import Image, ImageDraw, ImageTk
import random
from tkcolorpicker import askcolor

from convert.A import convertToA
from convert.B import convertToB
from convert.C import convertToC
from convert.D import convertToD
from convert.E import convertToE
from convert.F import convertToF
from convert.G import convertToG
from convert.H import convertToH
from convert.I import convertToI
from convert.J import convertToJ
from convert.L import convertToL
from convert.M import convertToM
from convert.O import convertToO
from convert.P import convertToP
from convert.S import convertToS
from convert.T import convertToT
from convert.U import convertToU
from convert.W import convertToW

CANVAS_HEIGHT = 700
CANVAS_WIDTH = 1000

class GUIProyectoFinal(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        
        self.colors=[]
        self.n_colores=0
        
        main_window.title("Proyecto Final")
        main_window.geometry('1000x700-150-30')
        
        self.c = Canvas(main_window, bg = "black", height = CANVAS_HEIGHT, width = CANVAS_WIDTH)
        self.c.grid(column=0, row=1)

        self.labelFrame = tk.LabelFrame(main_window)
        self.labelFrame.grid(column=0, row=0, sticky="w")

        self.txtPalabra=tk.Label(self.labelFrame, text="Palabra : ")
        self.txtPalabra.grid(column=0, row=0, padx=5, pady=5)

        self.palabra = tk.StringVar()
        self.entryPalabra = tk.Entry(self.labelFrame, width=10, justify=tk.RIGHT, textvariable=self.palabra)
        self.entryPalabra.grid(column=2, row=0, padx=5, pady=5)

        self.dibujar = Button(self.labelFrame, text="Dibujar", width=8, height=1, command=lambda: [self.c.delete("all"), self.longitud(self.palabra.get())])
        self.dibujar.grid(column=3, row=0, padx=5, pady=5)

        self.txtNColor =  tk.Label(self.c,text="número de colores: ")
        self.txtNColor.grid(column=5, row=0,padx=5,pady=5)

        self.NColores = tk.IntVar()
        self.entryNColores = tk.Entry(self.c, width=10, justify=tk.RIGHT, textvariable=self.NColores)
        self.entryNColores.grid(column=6, row=0, padx=5, pady=5)

        self.color = Button(self.c, text="Aceptar", width=8, height=1, command=self.color_pick)
        self.color.grid(column=7, row=0, padx=5, pady=5)

    def color_pick(self):
        
        
        for i in range(self.NColores.get()):
            self.colors.append(askcolor((255, 255, 0), self.c)[0])
        
        self.n_colores = len(texto) if self.NColores.get() > len(texto) or self.NColores.get()<=0 else self.NColores.get()

    def longitud(self, texto):
        texto = texto.upper()
        tmp = len(texto)

        if tmp == 4:
            print(4)
        elif tmp == 5:
            self.fractal5(texto)
        elif tmp == 6:
            print(6)
        elif tmp == 7:
            print(7)
        else:
            print("ERROR")

    def fractal5(self, texto):
        lineas = [[0, 0.1, -0.1, 0, -6.8, 7.7],  # Izquierda Arriba
        [0, 0.1, -0.1, 0, -6.8, 3.0],  # Izquierda Abajo
        [0.15, 0, 0, 0.07, -5, 8.7],  # Arriba
        [0, 0.1, -0.1, 0, -1.1, 7.7],  # Derecha Arriba
        [0, 0.1, -0.1, 0, -1.1, 3.0],  # Derecha Abajo
        [0.15, 0, 0, 0.07, -5, 3.6],  # Centro
        [0.15, 0, 0, 0.07, -5, -1], #Abajo
        [0, 0.1, -0.1, 0, -4, 7.7], # Linea de arriba hacia el centro (por ejemplo para la M)
        [0, 0.1, -0.1, 0, -4, 3.1], # Linea de abajo hacie el centro (por ejemplo para la W)

        [0, 0.1, -0.1, 0, 1.5, 7.7],  # Izquierda Arriba
        [0, 0.1, -0.1, 0, 1.5, 3.0],  # Izquierda Abajo
        [0.15, 0, 0, 0.07, 3.3, 8.7],  # Arriba
        [0, 0.1, -0.1, 0, 7.2, 7.7],  # Derecha Arriba
        [0, 0.1, -0.1, 0, 7.2, 3.0],  # Derecha Arriba
        [0.15, 0, 0, 0.07, 3.3, 3.6],  # Centro
        [0.15, 0, 0, 0.07, 3.3, -1], #Abajo
        [0, 0.1, -0.1, 0, 4.3, 7.7], # Linea de arriba hacia el centro (por ejemplo para la M)
        [0, 0.1, -0.1, 0, 4.3, 3.1], # Linea de abajo hacie el centro (por ejemplo para la W)

        [0, 0.1, -0.1, 0, 9.8, 7.7],  # Izquierda Arriba
        [0, 0.1, -0.1, 0, 9.8, 3.0],  # Izquierda Abajo
        [0.15, 0, 0, 0.07, 11.1, 8.7],  # Arriba
        [0, 0.1, -0.1, 0, 15.5, 7.7],  # Derecha Arriba
        [0, 0.1, -0.1, 0, 15.5, 3.0],  # Derecha Arriba
        [0.15, 0, 0, 0.07, 11.1, 3.6],  # Centro
        [0.15, 0, 0, 0.07, 11.1, -1], #Abajo
        [0, 0.1, -0.1, 0, 12.1, 7.7], # Linea de arriba hacia el centro (por ejemplo para la M)
        [0, 0.1, -0.1, 0, 12.1, 3.1], # Linea de abajo hacie el centro (por ejemplo para la W)

        [0, 0.1, -0.1, 0, 18.1, 7.7],  # Izquierda Arriba
        [0, 0.1, -0.1, 0, 18.1, 3.0],  # Izquierda Abajo
        [0.15, 0, 0, 0.07, 19.4, 8.7],  # Arriba
        [0, 0.1, -0.1, 0, 23.8, 7.7],  # Derecha Arriba
        [0, 0.1, -0.1, 0, 23.8, 3.0],  # Derecha Arriba
        [0.15, 0, 0, 0.07, 19.4, 3.6],  # Centro
        [0.15, 0, 0, 0.07, 19.4, -1], #Abajo
        [0, 0.1, -0.1, 0, 20.4, 7.7], # Linea de arriba hacia el centro (por ejemplo para la M)
        [0, 0.1, -0.1, 0, 20.4, 3.1], # Linea de abajo hacie el centro (por ejemplo para la W)

        [0, 0.1, -0.1, 0, 26.4, 7.7],  # Izquierda Arriba
        [0, 0.1, -0.1, 0, 26.4, 3.0],  # Izquierda Abajo
        [0.15, 0, 0, 0.07, 27.7, 8.7],  # Arriba
        [0, 0.1, -0.1, 0, 32.1, 7.7],  # Derecha Arriba
        [0, 0.1, -0.1, 0, 32.1, 3.0],  # Derecha Arriba
        [0.15, 0, 0, 0.07, 27.7, 3.6],  # Centro
        [0.15, 0, 0, 0.07, 27.7, -1], #Abajo
        [0, 0.1, -0.1, 0, 28.8, 7.7], # Linea de arriba hacia el centro (por ejemplo para la M)
        [0, 0.1, -0.1, 0, 28.8, 3.1], # Linea de abajo hacie el centro (por ejemplo para la W)
        ]

        listaChars = list(texto)

        for i in range (len(listaChars)):
            if listaChars[i] == 'A': lineas = convertToA(lineas, i)
            elif listaChars[i] == 'B': lineas = convertToB(lineas, i)
            elif listaChars[i] == 'C': lineas = convertToC(lineas, i)
            elif listaChars[i] == 'D': lineas = convertToD(lineas, i)
            elif listaChars[i] == 'E': lineas = convertToE(lineas, i)
            elif listaChars[i] == 'F': lineas = convertToF(lineas, i)
            elif listaChars[i] == 'G': lineas = convertToG(lineas, i)
            elif listaChars[i] == 'H': lineas = convertToH(lineas, i)
            elif listaChars[i] == 'I': lineas = convertToI(lineas, i)
            elif listaChars[i] == 'J': lineas = convertToJ(lineas, i)
            elif listaChars[i] == 'L': lineas = convertToL(lineas, i)
            elif listaChars[i] == 'M': lineas = convertToM(lineas, i)
            elif listaChars[i] == 'O': lineas = convertToO(lineas, i)
            elif listaChars[i] == 'P': lineas = convertToP(lineas, i)
            elif listaChars[i] == 'S': lineas = convertToS(lineas, i)
            elif listaChars[i] == 'T': lineas = convertToT(lineas, i)
            elif listaChars[i] == 'U': lineas = convertToU(lineas, i)
            elif listaChars[i] == 'W': lineas = convertToW(lineas, i)
        self.pintaIFS(lineas)

    def pintaIFS(self, mat):

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

        im = Image.new('HSV', (WIDTH, HEIGTH), (0, 0, 0))
        draw = ImageDraw.Draw(im)

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

            nx = int((x - xmin) / (xmax - xmin) * (WIDTH - 1))
            ny = (HEIGTH - 1) - int((y - ymin) / (ymax - ymin) * (HEIGTH - 1))
            if nx < (WIDTH-1) and ny < (HEIGTH-1):
                im.putpixel((int(nx), int(ny)), 255)
                draw.point([int(nx), int(ny)],self.colors[n_colores % index])

        self.imagen = ImageTk.PhotoImage(im)
        self.c.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=self.imagen)
        self.c.update()
        

main_window = tk.Tk()
app = GUIProyectoFinal(main_window)
app.mainloop()