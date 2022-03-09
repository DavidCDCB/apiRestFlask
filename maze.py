import time
import random
import turtle 

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

def get_espacios():
	espacios = []
	for i in range(len(m)):
		for j in range(len(m[0])):
			if(m[i][j] == " "):
				espacios.append((i,j))
	return len(espacios) > 0

def ruta(c,inicial,final,visitados):
	global m
	colors=["90","91","92","93","94","95","96"]
	color=random.choice(colors)


	stack = [inicial]
	recorrido = []
	aux = m[inicial[0]][inicial[1]]

	while(len(stack) > 0):
		n_coord = stack[-1]

		if(n_coord not in recorrido):
			recorrido.append(n_coord)
	
		m[n_coord[0]][n_coord[1]] = c
		verM(m,c,color)
		time.sleep(1/20)

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

def get_steps(camino):
	steps = [camino[0],camino[-1]]
	if(len(camino) > 1):
		for i in range(0,len(camino)-1):
			if(camino[i][0] < camino[i+1][0]):
				steps.append([camino[i],"d"])
			elif(camino[i][0] > camino[i+1][0]):
				steps.append([camino[i],"u"])
			elif(camino[i][1] < camino[i+1][1]):
				steps.append([camino[i],"r"])
			elif(camino[i][1] > camino[i+1][1]):
				steps.append([camino[i],"l"])
	else:
		steps = [camino[0]]
	return steps

def graficar(rutas):
	global lim
	ancho = (lim*450)//20
	alto = (lim*450)//20 
	wn=turtle.Screen()
	turtle.setup(width=ancho, height=alto)
	wn.bgcolor("grey")
	turtle.speed(0)
	turtle.pensize(10)
	
	for ruta in rutas[::-1]:
		turtle.color("black")
		turtle.penup()
		turtle.setpos(((ruta[0][1])*20-(ancho//2)+30,(alto//2)-20*(ruta[0][0])-30))

		turtle.speed(1)
		for s in ruta:
			turtle.color("white")
			turtle.pendown()
			turtle.setpos(((s[1])*20-(ancho//2)+30,(alto//2)-20*(s[0])-30))
			turtle.penup()
	wn.exitonclick()


lim = 20
m = crearM(lim,lim)
final = 0

caminos_stack = []
completados = []
ind = 0
caracter = 0

nuevos = ruta(str(ind),(0,0),(lim-1,lim-1),[(0,0)]).copy()
ind += 1
caracter += 1


while(get_espacios() or ind < len(completados)):
	
	if(len(nuevos) == 1):
		if(check(caminos_stack,nuevos[0])==False):
			caminos_stack.append(nuevos)
	else:
		caminos_stack.append(nuevos)

	for n in nuevos:
		if(n not in completados):
			completados.append(n)

	if(ind < len(completados)):
		nuevos = ruta(str(caracter),completados[ind],None,completados.copy()).copy()
		ind += 1

	if(len(nuevos) > 1):
		caracter += 1

# Inicio,Final y pasos
for c in caminos_stack:
	print("->",caminos_stack.index(c))
	print(c)
	#print(get_steps(c))

graficar(caminos_stack)


'''
while(len(nuevos) <= 1):
	print(random.choice(caminos_stack[-1]))
	nuevos = ruta(str(ind),random.choice(caminos_stack[-1]),None,completados).copy()
'''





'''
espacios = []
espacios = get_espacios()
ruta("1",random.choice(espacios),random.choice(espacios))

espacios = []
espacios = get_espacios()
ruta("2",random.choice(espacios),random.choice(espacios))

espacios = []
espacios = get_espacios()
ruta("3",random.choice(espacios),random.choice(espacios))

def c_wall(l,c,v):
	cad = ""
	for x in l:
		if(x == 0):
			cad += v
		else:
			cad += c
	return cad


paredes = [random.randint(0,1) for x in range(5)]
print("|"+c_wall(paredes," |","  "))
suelos = [random.randint(0,1) for x in range(5)]
print(c_wall(suelos,"+-","+ ")+"+")

print(paredes)
print(suelos)'''

