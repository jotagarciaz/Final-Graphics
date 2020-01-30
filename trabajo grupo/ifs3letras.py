# IFS fractals
# FB - 201003221
from PIL import Image
import random


class IFS:
	def __init__(self):
		self.mat = [
			
			
						[0.1,0,0,0.1,-6,8,0.05225806452], #J top
						[0,0.065,-0.24,0,-6,6.4,0.05225806452], #J v
						[0.08,0,0,0.1,-6,4.1,0.05225806452], # J bot

						[0.1,0,0,0.1,-1.8,8,0.05225806452], #G top
						[0,0.065,-0.24,0,-2.6,6.1,0.05225806452], #G v l
						[0.1,0,0,0.1,-2,4,0.05225806452],	#G bot
						[0, 0.06, -0.1, 0, -1.1, 4, 0.05225806452], #G v r
						[0.06, 0, 0, 0.06, -1, 5, 0.05225806452],# G v mid

						[0.1, 0, 0, 0.1, 2.3, 8, 0.05225806452], # A top
						[0,0.065,-0.32,0,1.4,6,0.05225806452], # A v l
						[0,0.065,-0.32,0,3.0,6,0.05225806452], # A vertical right
						[0.05, 0, 0, 0.06, 2.5, 5, 0.05225806452] # A mid



					
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