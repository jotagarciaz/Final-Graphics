# IFS fractals
# FB - 201003221
from PIL import Image
import random

# he tenido que ajustar el inferior de la J, C, G , I pasando la y de -0.8 a 0

class IFS:
	def __init__(self):
		self.mat = [
			
			
						[0.1,0,0,0.1,-6,8,0.03225806452], #J top
						[0,0.08,-0.24,0,-4.5,6.1,0.03225806452], #J v
						[0.08,0,0,0.1,-6,0,0.03225806452], # J bot

						[0.1,0,0,0.1,-2,8,0.03225806452], #G top
						[0,0.08,-0.24,0,-2.6,6.1,0.03225806452], #G v l
						[0.1,0,0,0.1,-2,0,0.03225806452],	#G bot
						[0, 0.06, -0.1, 0, -0.1, 2.6, 0.03225806452], #G v r
						[0.06, 0, 0, 0.06, -1, 3.5, 0.03225806452],# G v mid

						[0.1, 0, 0, 0.1, 2, 8, 0.03225806452], # A top
						[0,0.08,-0.28,0,1.4,6,0.03225806452], # A v l
						[0,0.08,-0.28,0,3.8,6,0.03225806452], # A vertical right
						[0.05, 0, 0, 0.06, 2.5, 3.6, 0.03225806452], # A mid

						[0.1,0,0,0.1,6,8,0.03225806452],#R top
						[0,0.08,-0.28,0,5.4,6.0,0.03225806452],#R v left
						[0,0.08,-0.16,0,8,7.0,0.03225806452],#R v r
						[0.06, 0, 0, 0.06, 6.5, 3.6, 0.03225806452],#R mid
						[0.065,0.05,-0.12,0.065,6.8,2,0.03225806452],#R angle

						[0.1, 0, 0, 0.1, 10, 8, 0.03225806452],#C top
						[0,0.08,-0.24,0,9.4,6.1,0.03225806452],#C v 
						[0.1, 0, 0, 0.1, 10, 0, 0.03225806452],#C bot
						

						[0.1, 0, 0, 0.1, 14, 8, 0.03225806452],#I  top
						[0,0.08,-0.24,0,14.5,6.1,0.03225806452],#I v
						[0.1, 0, 0, 0.1, 14, 0, 0.03225806452],#I bot 
						

						[0.1, 0, 0, 0.1, 18, 8, 0.03225806452], # A top
						[0,0.08,-0.28,0,17.4,6,0.03225806452], # A V left
						[0.05, 0, 0, 0.06, 18.5, 3.6, 0.03225806452], # A mid
						[0,0.08,-0.28,0,19.8,6,0.03225806452] # A V right
						
						


				
					
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