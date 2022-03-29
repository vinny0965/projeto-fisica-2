from vpython import *;

#objetos
bola = sphere(pos=vec(0,1,0), radius=1, color=color.red, make_trail=True)
solo = box(pos=vec(0,0,0),size=vec(80,0.5,5),color=color.white)

#funções
executar = False
def exetuar_btn():
    global executar
    executar = True


#botao

button(text="Excecutar",bind = exetuar_btn)


#Condições iniciais

theta = 45*(pi/180)  #30 é o ângulo de 30 graus, multiplicamos por Pi dividindo por 180 para ter o resultado em radiano
g = vec(0,-9.8,0)  #aceleração da gravidade no eixo y
bola.v = vec(20*cos(theta),20*sin(theta),0) #velocidade inicial da bola
t = 0 #tempo inicial
dt = 0.001 #acrecimo de tempo

#legenda
legenda = label(pos=vec(0,-20,0),text="Distancia em X")
legendaVelY = label(pos=vec(0,-10,0), text="Velocidade em Y")
legendaDisY = label(pos=vec(0,-15,0),text="Distancia em Y")
legendaVelX = label(pos=vec(0,-25,0), text="Velocidade em X")

#graficos
grafico1= graph(xtitle='alcance  em (X) ',ytitle='altura em (Y)')
grafico_1 = gcurve(graph=grafico1,color = color.red)

grafico2= graph(xtitle='tempo ',ytitle='posicao em (Y)')
grafico_2 = gcurve(graph=grafico2,color = color.red)

grafico3= graph(xtitle='tempo ',ytitle='Velocidade em (Y)')
grafico_3 = gcurve(graph=grafico3,color = color.red)

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
        legenda.text = "Distância percorrida em X = {:0.3f} m".format(bola.pos.x)
        legendaDisY.text = "Distância percorrida em Y = {:0.3f} m".format(bola.pos.y)
        legendaVelY.text = "velocidade componente Y = {:0.3f}".format(bola.v.y)
        legendaVelX.text = "velocidade componente X = {:0.3f}".format(bola.v.x)

        grafico_1.plot(bola.pos.x,bola.pos.y)
        grafico_2.plot(t,bola.pos.y)
        grafico_3.plot(t,bola.v.y)





