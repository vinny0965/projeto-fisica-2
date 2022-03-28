from vpython import *;

#objetos
bola = sphere(pos=vec(0,1,0), radius=1, color=color.red, make_trail=True)
solo = box(pos=vec(0,0,0),size=vec(75,0.5,5),color=color.white)

#funções
executar = False
def exetuar_btn():
    global executar
    executar = True


#botao

button(text="Excecutar",bind = exetuar_btn)


#Condições iniciais

theta = 30*(pi/180)
g = vec(0,-9.8,0)  #acelereção da gravidade
bola.v = vec(20*cos(theta),20*sin(theta),0) #velocidade inicial da bola
t = 0 #tempo inicial
dt = 0.001 #acrecimo de tempo

#legenda
legenda = label(pos=vec(0,20,0),text="Distancia em X")

legendaVel = label(pos=vec(0,10,0), text="Velocidade")

#setas

bola.ex = vector(20*cos(theta),0,0)
attach_arrow(bola,"ex",color=color.blue,shaftwidth=0.5)

bola.ey = vector(0,20*sin(theta),0)
attach_arrow(bola,"ey",color=color.green,shaftwidth=0.5)

#equacoes

while bola.pos.y >=0.5:
    rate(500)
    if executar:
        bola.v = bola.v + g*dt
        bola.pos = bola.pos + bola.v * dt

        bola.ey = bola.ey+g*dt
        t = t + dt
        legenda.text = "x = {:0.3f} m".format(bola.pos.x)
        legendaVel.text = "velocidade = {:0.3f}".format(bola.v.y)




