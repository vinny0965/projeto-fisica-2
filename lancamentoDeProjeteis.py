"""

 _      __    _      __     __    _      ____  _     _____  ___       ___   ____      ___   ___   ___     _   ____ _____  ____  _   __
| |    / /\  | |\ | / /`   / /\  | |\/| | |_  | |\ |  | |  / / \     | | \ | |_      | |_) | |_) / / \   | | | |_   | |  | |_  | | ( (`
|_|__ /_/--\ |_| \| \_\_, /_/--\ |_|  | |_|__ |_| \|  |_|  \_\_/     |_|_/ |_|__     |_|   |_| \ \_\_/ \_|_| |_|__  |_|  |_|__ |_| _)_)

"""

from vpython import *

#objetos

#
solo = box(pos=vec(0,0,0),size=vec(80,0.5,5),color=color.white)
bola = sphere(pos=vec(0,1,0), radius=1, color=color.red, make_trail=True)

#função para executar o codigo
executar = False
def executar_btn():
    global executar
    executar = True


def anexar():
    pass

#função executar o botão salvar dados
dados_alternativo = False
def alterar_dados_btn():
    global dados_alternativo
    dados_alternativo = True

#função para criar espaços na vertical
def vSpace(times):
    # espaço na vertical
    scene.append_to_caption(f'\n' * times)

#função para criar espaços na horizontal
def hSpace(times):
    # espaço na horizontal
    scene.append_to_caption(f' ' * times)

#botão executar e alterar dados
vSpace(1)
button(text="Executar",bind = executar_btn)
hSpace(1)
button(text="Alterar Dados",bind = alterar_dados_btn)


#texto angulo
angulo_texto = wtext(text="Digite o ângulo ex:45:")

#textfield para angulo
angulo_field = winput(bind = anexar(), type="numeric",width=50,_height=20)

#texto velocidade:
velocidade_texto = wtext(text="Digite a velocidade inicial:")

#textfield para velocidade
velocidade_field = winput(bind = anexar(),type = "numeric",width=50,_height=20)
vSpace(2)

#legendas para valores do alcance/velocidades/distâncias percorridas
alcance_R_text = wtext(text=" Alcance R em X - ")
vSpace(1)
velocidade_Y_text = wtext(text="Velocidade componente Y - ")
vSpace(1)
distancia_Y_text = wtext(text="Distância percorrida em Y - ")
vSpace(1)
velocidade_X_text = wtext(text="Velocidade componente X - ")
vSpace(2)
tempo_total_texto = wtext(text=" Tempo total: - s")
alcance_R_texto = wtext(text=" /Alcance R: - m")
altura_max_texto = wtext(text=" /Altura  Máxima: - m")
vSpace(2)


#ponteiro aceleracao da gravidade
pointer = arrow(pos=vector(-10,20,10),axis=vector(5,0,0), shaftwidth=1,up = vector(2,0,0))
legenda_pointer = label(pos=vec(-20,22,0),text="g = -9.8")


#Condições iniciais

theta = 45*(pi/180)  #45 é o ângulo de 30 graus, multiplicamos por Pi dividindo por 180 para ter o resultado em radiano/ Obs: este é o ângulo padrão, caso necessário pode alterar na animação
g = vec(0,-9.8,0)  #aceleração da gravidade no eixo y
bola.v = vec(20*cos(theta),20*sin(theta),0) #velocidade inicial da bola
t = 0 #tempo inicial
dt =0.001 #acrecimo de tempo
tempoTotal = (bola.v.y / -g.y) * 2  # calculando o tempo total do lançamento
alcanceR = bola.v.x * tempoTotal #calculando o alcance da bola R  na horizontal
altura_max = (bola.v.y ** 2) / (-2 * g.y) #calculando a altura máxima da bola em Y

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

        #calculando  e atualizando a velocidade da bola
        bola.v = bola.v + g*dt
        #calculando  e atualizando a posição da bola
        bola.pos = bola.pos + bola.v * dt
        #atualizando seta em direção a bola
        bola.ey = bola.ey+g*dt
        #acrécimo de tempo ao tempo final
        t = t + dt
        #atualizando texto da seta da componente Y
        text_seta.pos = vec(bola.pos.x, bola.ey.y-2, 0)
        #atualizando texto da seta da componente X na horizontal
        text_seta_horizontal.pos = vec(bola.pos.x+10 + 1, bola.pos.y+2, 0)

        #verificando e comparando tamanho do chão com o da bola para aumentar o chão automaticamente
        if bola.pos.x > solo.pos.x+solo.size.x*0.5 or bola.pos.x < solo.pos.x-solo.size.x*0.5:
            solo.size=vec(bola.pos.x*2,0.5,5)

        #atualizando informações do movimento, alcance, velocidades e distâncias
        alcance_R_text.text = "Alcance R em X = {:0.2f} m".format(bola.pos.x)
        velocidade_Y_text.text = "Velocidade componente Y = {:0.2f}".format(bola.v.y)
        distancia_Y_text.text = "Distância percorrida em Y = {:0.2f} m".format(bola.pos.y-1)
        velocidade_X_text.text = "Velocidade componente X = {:0.2f}".format(bola.v.x)

        #plotando e exibindo as atualizações dos gráficos na tela
        grafico_3.plot(t, bola.v.y)
        grafico_2.plot(t,bola.pos.y-1)
        grafico_1.plot(t, bola.pos.x)

    #verificando se foi digitado o ângulo e a velocidade inicial para execução do código
    if dados_alternativo:
        #atribuindo valor ao ângulo theta recebido do field digitado pelo o usuário
        theta = (float(angulo_field.text) * (pi / 180))
        #atualizando a velocidade inical da bola recebida do field digitado pelo o usuário
        bola.v = vec(float(velocidade_field.text) * cos(theta), float(velocidade_field.text) * sin(theta),0)  # velocidade inicial da bola
        #atualizando o tempo total do movimento
        tempoTotal = (bola.v.y / -g.y) * 2  # calculando o tempo total do lançamento
        #atualizando o alcance total do movimento
        alcanceR = bola.v.x * tempoTotal  # calculando o alcance R
        #calculando a altura máxima da bola
        altura_max = (bola.v.y ** 2) / (-2 * g.y)
        dados_alternativo = False


vSpace(1)
#altualizando dados dos cálculos do tempo total, o alcance e  a altura máxima que a bola atingiu
tempo_total_texto.text = "Tempo total: {:0.2f} s".format(tempoTotal)
alcance_R_texto.text = " /Alcance R: {:0.3f} m".format(alcanceR)
altura_max_texto.text = " /Altura  Máxima: {:0.2f} m".format(altura_max)




