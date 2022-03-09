import time
import random
import turtle #sudo apt install python-tk
from PIL import Image

def crearM(f,c):
	m=[[" "] * c for i in range(f)]
	return m

def verM(m,c,color):
	cad=""
	lin=""
	for i in range((len(m)*2)+10):
		lin+="-"
	print(lin)

	for i in range(len(m)):
		for j in range(len(m[0])):
			if(m[i][j]==" "):cad+="   "
			else:
				if(m[i][j]==c):
					if(len(m[i][j])>1):cad+="\033["+color+"m"+m[i][j]+' \033[0m'
					else:cad+="\033["+color+"m "+m[i][j]+' \033[0m'
				else:
					if(len(m[i][j])>1):cad+=m[i][j]+" "
					else:cad+=" "+m[i][j]+" "
		print("|"+cad+"|")
		cad=""
	print(lin)

def get_espacios():
	espacios = []
	for i in range(len(m)):
		for j in range(len(m[0])):
			if(m[i][j] == " "):
				espacios.append((i,j))
	return len(espacios) > 0

def get_adyacentes(c,visitados):
	global lim

	l_adyacentes = []
	l_adyacentes.append((c[0]-1,c[1]))
	l_adyacentes.append((c[0]+1,c[1]))
	l_adyacentes.append((c[0],c[1]-1))
	l_adyacentes.append((c[0],c[1]+1))

	def criterio(x):
		if(x[0] >= 0 and x[0] < lim):
			if(x[1] >= 0 and x[1] < lim):
				if(x not in visitados):
					visitados.append(x)
					return True
		return False

	elements = list(filter(criterio, l_adyacentes))
	return random.sample(elements,len(elements))


def ruta(c,inicial,final,visitados):
	global m

	stack = [inicial]
	recorrido = []
	aux = m[inicial[0]][inicial[1]]

	while(len(stack) > 0):
		n_coord = stack[-1]

		if(n_coord not in recorrido):
			recorrido.append(n_coord)
	
		m[n_coord[0]][n_coord[1]] = c

		if(final != None):
			if(n_coord == final):
				break

		adyacentes = get_adyacentes(n_coord,visitados)

		if(len(adyacentes) > 0):
			stack += adyacentes
		else:
			if(final == None):
				break
			else:
				deleted = stack.pop()
				recorrido.pop()
				m[deleted[0]][deleted[1]] = " "

	if(len(recorrido) == 1 and aux != " "):
		m[inicial[0]][inicial[1]] = aux

	return recorrido

def check(caminos_stack,element):
	for i in caminos_stack:
		for j in i:
			if(j == element):
				return True
	return False

def graficar(rutas):
	global lim
	ancho = (lim*450)//20
	alto = (lim*450)//20 
	wn=turtle.Screen()
	turtle.setup(width=ancho, height=alto)
	wn.bgcolor("grey")
	turtle.speed(0)
	turtle.pensize(10)
	turtle.ht()
	turtle.speed(5)
	for ruta in rutas:
		turtle.color("green")
		turtle.penup()
		turtle.setpos(((ruta[0][1])*20-(ancho//2)+30,(alto//2)-20*(ruta[0][0])-30))
		for s in ruta:
			turtle.color("green")
			turtle.pendown()
			turtle.setpos(((s[1])*20-(ancho//2)+30,(alto//2)-20*(s[0])-30))
			turtle.penup()
	turtle.getscreen()
	turtle.getcanvas().postscript(file="preImage.eps")


	TARGET_BOUNDS = (1024, 1024)

	pic = Image.open('preImage.eps')
	pic.load(scale=10)

	if pic.mode in ('P', '1'):
		pic = pic.convert("RGBA")

	ratio = min(TARGET_BOUNDS[0] / pic.size[0],TARGET_BOUNDS[1] / pic.size[1])
	new_size = (int(pic.size[0] * ratio), int(pic.size[1] * ratio))

	pic = pic.resize(new_size, Image.ANTIALIAS)
	d = pic.getdata()

	new_image = []
	for item in d:
		if item[0] in list(range(200, 256)):
			new_image.append((0, 0, 0))
		elif(item[1] == 128):
			new_image.append((255, 255, 255))
		else:
			new_image.append(item)

	pic.putdata(new_image)
	pic.save("image.png")



lim = int(input("Tamaño del laberinto (>15): "))
m = crearM(lim,lim)
final = 0

caminos_stack = []
completados = []
ind = 0
caracter = 0

nuevos = ruta(str(ind),(0,0),(lim-1,lim-1),[(0,0)])[:]
ind += 1
caracter += 1

colors=["90","91","92","93","94","95","96"]

while(get_espacios()):
	
	#time.sleep(1/20)
	if(len(nuevos) > 1):
		caminos_stack.append(nuevos)

	for n in nuevos:
		if(n not in completados):
			completados.append(n)

	nuevos = ruta(str(caracter),random.choice(completados),None,completados[:])[:]

	if(len(nuevos) > 1):
		verM(m,str(caracter),random.choice(colors))
		caracter += 1
		

	

caminos_stack.append(nuevos)

for c in caminos_stack:
	print("->",caminos_stack.index(c))
	print(c)

graficar(caminos_stack)
