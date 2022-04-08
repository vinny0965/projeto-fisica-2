"""

 _      __    _      __     __    _      ____  _     _____  ___       ___   ____      ___   ___   ___     _   ____ _____  ____  _   __
| |    / /\  | |\ | / /`   / /\  | |\/| | |_  | |\ |  | |  / / \     | | \ | |_      | |_) | |_) / / \   | | | |_   | |  | |_  | | ( (`
|_|__ /_/--\ |_| \| \_\_, /_/--\ |_|  | |_|__ |_| \|  |_|  \_\_/     |_|_/ |_|__     |_|   |_| \ \_\_/ \_|_| |_|__  |_|  |_|__ |_| _)_)

"""

from vpython import *

#objetos

solo = box(pos=vec(0,0,0),size=vec(80,0.5,5),color=color.white)
bola = sphere(pos=vec(0,1,0), radius=1, color=color.red, make_trail=True)
#funções
executar = False
def executar_btn():
    global executar
    executar = True

def anexar():
    pass

angulo_alternativo = False
def angulo_btn():
    global angulo_alternativo
    angulo_alternativo = True

velocidade_alternativa = False
def velocidade_btn():
    global velocidade_alternativa
    velocidade_alternativa = True


#def calcular_com_velocidade_inicial(velocidade_digitada): - essa velocidade seria o velocidade_field.text que está no while lá em baixo,
#ao clicar em velocidade_btn ele vai fazer as mesmas coisas que o executar faz, porém com essa velocidade passada pelo usuário

#botao

button(text="Executar",bind = executar_btn)
button(text="Alterar Angulo",bind = angulo_btn)
button(text="Alterar Velocidade",bind = velocidade_btn)

#texto angulo
angulo_texto = wtext(text="Digite o ângulo ex:45:")

#textfield para angulo
angulo_field = winput(bind = anexar(), type="numeric",width=50,_height=20)

#texto velocidade:
velocidade_texto = wtext(text="Digite a velocidade inicial:")

#textfield para velocidade
velocidade_field = winput(bind = anexar(),type = "numeric",width=50,_height=20)


#Condições iniciais

theta = 45*(pi/180)  #45 é o ângulo de 30 graus, multiplicamos por Pi dividindo por 180 para ter o resultado em radiano
g = vec(0,-9.8,0)  #aceleração da gravidade no eixo y
bola.v = vec(20*cos(theta),20*sin(theta),0) #velocidade inicial da bola
t = 0 #tempo inicial
dt =0.001 #acrecimo de tempo
tempoTotal = (bola.v.y / -g.y) * 2  # calculando o tempo total do lançamento
alcanceR = bola.v.x * tempoTotal #calculando o alcance da bola R  na horizontal
altura_max = (bola.v.y ** 2) / (-2 * g.y) #calculando a altura máxima da bola em Y

#legenda
legenda = label(pos=vec(0,-20,0),text="Alcance R em X")
legendaVelY = label(pos=vec(0,-10,0), text="Velocidade em Y")
legendaDisY = label(pos=vec(0,-15,0),text="Distancia em Y")
legendaVelX = label(pos=vec(0,-25,0), text="Velocidade em X")

#graficos

grafico2= graph(xtitle='tempo (s)',ytitle='posicao em Y (m)')
grafico_2 = gcurve(graph=grafico2,color = color.red)

grafico1= graph(xtitle='tempo (s)',ytitle='alcance R (m)')
grafico_1 = gcurve(graph=grafico1,color = color.red)

grafico3= graph(xtitle='tempo (s)',ytitle='Velocidade em Y (m)')
grafico_3 = gcurve(graph=grafico3,color = color.red)

#setas

bola.ex = vector(20*cos(theta),0,0)
attach_arrow(bola,"ex",color=color.blue,shaftwidth=0.5)

bola.ey = vector(0,20*sin(theta),0)
attach_arrow(bola,"ey",color=color.green,shaftwidth=0.5)

text_seta = text(text='Voy',align='center', color=color.green)
text_seta.pos = vec(bola.pos.x, bola.ey.y+2, 0)

text_seta_horizontal = text(text='Vx',align='center', color=color.green)
text_seta_horizontal.pos = vec(bola.ex.x+1, 1, 0)
#equacoes

while bola.pos.y >=1:
    rate(500)
    if executar:

        bola.v = bola.v + g*dt
        bola.pos = bola.pos + bola.v * dt
        bola.ey = bola.ey+g*dt
        t = t + dt
        text_seta.pos = vec(bola.pos.x, bola.ey.y-2, 0)
        text_seta_horizontal.pos = vec(bola.pos.x+10 + 1, bola.pos.y+2, 0)
        solo.size=vec(bola.pos.x*2,0.5,5)
        legenda.text = "Distância percorrida em X = {:0.2f} m".format(bola.pos.x)
        legendaDisY.text = "Distância percorrida em Y = {:0.2f} m".format(bola.pos.y-1)
        legendaVelY.text = "velocidade componente Y = {:0.2f}".format(bola.v.y)
        legendaVelX.text = "velocidade componente X = {:0.2f}".format(bola.v.x)

        grafico_3.plot(t, bola.v.y)
        grafico_2.plot(t,bola.pos.y-1)
        grafico_1.plot(t, bola.pos.x)

    if angulo_alternativo:
        theta = (float(angulo_field.text) * (pi / 180))
        angulo_alternativo = False

    if velocidade_alternativa:
        bola.v = vec(float(velocidade_field.text) * cos(theta), float(velocidade_field.text) * sin(theta), 0)  # velocidade inicial da bola
        velocidade_alternativa = False
        #usa essa "velocidade_digitada" na função calcular_com_velocidade_inicial(velocidade_digitada) e gg;
        tempoTotal = (bola.v.y / -g.y) * 2  # calculando o tempo total do lançamento
        alcanceR = bola.v.x * tempoTotal  # calculando o alcance R
        altura_max = (bola.v.y**2)/(-2*g.y)


tempo_total_texto = wtext(text=" Tempo total: {:0.2f} s".format(tempoTotal))
alcance_R_texto = wtext(text=" /Alcance R: {:0.3f} m".format(alcanceR))
altura_max_texto = wtext(text=" /Altura  Máxima: {:0.2f} m".format(altura_max))



