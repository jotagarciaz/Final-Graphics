# IFS fractals
# FB - 201003221
from PIL import Image
import random


# En este caso habría que hacer los mismos ajustes que en el anterior, pudiendo omitirse el ajuste de tamaño de R angle ajustando eso si la posicion en x e y
# he tenido que ajustar el inferior de la J, C, G , I pasando la y de 
# he tenido que ajustar el vertical hacia la izquierda de la J passndo de   de G v r paso de A vertical right pasa de  R v r pasa de  a 
# hay que subir las barras horizontales de la A, la R y la G
# hay que ajustar la vertical derecha de G y R
# hay que ajustar el top de G,A,R , moviendolos hacia la derecha
# hay que ajustar la vertical de la C

class IFS:
	def __init__(self):
		self.mat = [
			
			
						[0.1,0,0,0.1,-6,8,0.03225806452], #J top
						[0,0.08,-0.24,0,-5.6,6.1,0.03225806452], #J v
						[0.08,0,0,0.1,-6,2,0.03225806452], # J bot

						[0.1,0,0,0.1,-1.8,8,0.03225806452], #G top
						[0,0.08,-0.24,0,-2.6,6.1,0.03225806452], #G v l
						[0.1,0,0,0.1,-2,2,0.03225806452],	#G bot
						[0, 0.06, -0.1, 0, -0.6, 3.6, 0.03225806452], #G v r
						[0.06, 0, 0, 0.06, -1, 4.5, 0.03225806452],# G v mid

						[0.1, 0, 0, 0.1, 2.3, 8, 0.03225806452], # A top
						[0,0.08,-0.28,0,1.4,6,0.03225806452], # A v l
						[0,0.08,-0.28,0,3.0,6,0.03225806452], # A vertical right
						[0.05, 0, 0, 0.06, 2.5, 4.6, 0.03225806452], # A mid

						[0.1,0,0,0.1,6.3,8,0.03225806452],#R top
						[0,0.08,-0.28,0,5.4,6.0,0.03225806452],#R v left
						[0,0.08,-0.16,0,7,7.0,0.03225806452],#R v r
						[0.06, 0, 0, 0.06, 6.5, 4.6, 0.03225806452],#R mid
						[0.035,0.05,-0.09,0.035,6.8,3.90,0.03225806452],#R angle

						[0.1, 0, 0, 0.1, 10, 8, 0.03225806452],#C top
						[0,0.08,-0.24,0,9.2,6.1,0.03225806452],#C v 
						[0.1, 0, 0, 0.1, 10, 2, 0.03225806452]#C bot
						
						
						
			
					
			]

	def inserta_ifs(self,a,b,c,d,e,f,p):
		self.mat.append([a,b,c,d,e,f,p])
	
	def genera_ifs(self):
		# image size
		imgx = 1400
		imgy = 800 # will be auto-re-adjusted
		
		m = len(self.mat)
		# find the xmin, xmax, ymin, ymax
		x = self.mat[0][4]
		y = self.mat[0][5]
		#
		xa = x
		xb = x
		ya = y
		yb = y
		#
		for k in range(imgx * imgy):
			p=random.random()
			psum = 0.0
			for i in range(m):
				psum += self.mat[i][6]
				if p <= psum:
					break
			x0 = x * self.mat[i][0] + y * self.mat[i][1] + self.mat[i][4]
			y  = x * self.mat[i][2] + y * self.mat[i][3] + self.mat[i][5]
			x = x0
			#
			if x < xa:
				xa = x
			if x > xb:
				xb = x
			if y < ya:
				ya = y
			if y > yb:
				yb = y
		
		# drawing
		imgy = round(imgy * (yb - ya) / (xb - xa)) # auto-re-adjust the aspect ratio
		image = Image.new("L", (imgx,imgy))
		
		x=0.0
		y=0.0
		for k in range(imgx * imgy):
			p=random.random()
			psum = 0.0
			for i in range(m):
				psum += self.mat[i][6]
				if p <= psum:
					break
			x0 = x * self.mat[i][0] + y * self.mat[i][1] + self.mat[i][4]
			y  = x * self.mat[i][2] + y * self.mat[i][3] + self.mat[i][5]
			x = x0
			jx = int((x - xa) / (xb - xa) * (imgx - 1))
			jy = (imgy - 1) - int((y - ya) / (yb - ya) * (imgy - 1))
			image.putpixel((jx, jy), 255)
		
		image.save("IFS.png")
		image.show()

if __name__ == "__main__":
	ifs = IFS()
	#ifs.inserta_ifs()
	ifs.genera_ifs()