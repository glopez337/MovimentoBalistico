from time import sleep
import math

def main():
  print("*OBSERVAÇÃO: A resistência do ar está sendo desconsiderada para a obtenção de resultados.\n \n")
  sleep(3)

  #Obs colocar o valor em metros.
  h_solo = float(input("1) Digite a altura de lançamento a partir do solo (Em metros): "))

  v0 = float(input("2) Digite a velocidade de lançamento inicial (Em m/s): "))

  ang = float(input("3) Digite o ângulo do lançamento (entre 0 e 90 graus): "))

  td = float(input("4) Digite um instante qualquer, em segundos, após o lançamento: "))

  g = 9.8
  print("\n\n_________________________________")
  print("DADOS RECEBIDOS PELO USUÁRIO:")
  print("Altura do solo: %.3f metros"%h_solo)
  print("Velocidade de lançamento inicial: %.1f m/s"%v0)
  print("Ângulo de lançamento: %.3f graus"%ang)
  print("Instante escolhido: %.3f segundos"%td)
  print("_________________________________\n\n")

  #CÁLCULO PARA OBTER v0x E v0y
  sen_ang = math.sin(math.radians(ang))
  cos_ang = math.cos(math.radians(ang))
  #o math.sin e math.cos tomam o ângulo base como radiano
  #então converter o ângulo em graus p radianos pra funcionar
  v0x = v0*cos_ang
  v0y = v0*sen_ang

  print("CÁLCULOS:\n\n")
  print("_________________________________")
  print("Componentes da velocidade inicial:\nComponente x = %.3f m/s\nComponente y = %.3f m/s"%(v0x,v0y))
  print("_________________________________\n")

  #CÁLCULO PARA OBTER POSIÇÕES X E Y NO TEMPO ESCOLHIDO
  x = v0x*td
  y = h_solo + v0y*td - (g*td**2)/2

  print("_________________________________")
  print("Posição no tempo escolhido (%.3f segundos)"%td)
  print("Em X = %.3f"%x)
  print("Em Y = %.3f"%y)
  print("_________________________________\n")
  


 #CÁLCULO PARA OBTER TEMPO NO AR E ALCANCE
 #bhaskara com a fórmula do muv, com os valores do eixo y
 # 0 = altura do solo + v0y.t -10t²/2 (MUV)
 # -5t² + v0y.t + altura do solo
 # a = -5 | b = v0y | c = altura do solo
  a = -4.9
  b = v0y
  c = h_solo

  #serão gerados 2 valores, onde um é negativo.
  t1 = (-b+ math.sqrt((b**2)-4*a*c))/-g
  t2 = (-b- math.sqrt((b**2)-4*a*c))/-g
 
  #N existe tempo negativo, ent a resp é o outro
  t_no_ar = 0
  if t1>t2:
    t_no_ar = t1
  else:
    t_no_ar = t2


  print("Tempo no ar: %.3f segundos"%t_no_ar)

  #não há aceleração no movimento horizontal
  #então, alcance = v_horizontal*tempo
  alcance = v0x*t_no_ar
  print("Alcance máximo = %.3f metros"%alcance)


  #CÁLCULO PARA ALTURA MÁXIMA
  #v0².sen²(angulo) / 2g
  #no fim, somar com a altura que o lançamento começou
  h_max = (((v0*v0)*(sen_ang*sen_ang))/(2*g))+h_solo
  print("Altura máxima: %.3f metros"%h_max)


  #CÁLCULO PARA OBTER Vx E Vy NO TEMPO ESCOLHIDO

  vx = x/td
  vy = 2*(((y-h_solo)/td)-v0y/2)

  modulo = math.sqrt(vx**2+vy**2)

  print("_________________________________")
  print("Velocidade no tempo escolhido pelo usuário:")
  print("Componente x = %.3f m/s"%vx)
  print("Componente y = %.3f m/s"%vy)
  print("Módulo = %.3f m/s"%modulo)
  print("_________________________________\n")



  #COMPONENTES DE V NA ALTURA MÁXIMA
  #Na altura máxima vy é sempre 0, e vx = v0x
  #Pelo fato de vy=0 , módulo = vx

  print("_________________________________")
  print("Velocidade na altura máxima")
  print("Componente x = %.3f m/s\nComponente y = 0"%v0x)
  print("Módulo da Velocidade: %.3f m/s"%v0x)
  print("_________________________________\n")

  #COMPONENTES DE V AO ATINGIR O CHÃO
  #vx continua = v0x

  yf = h_solo + v0y*t_no_ar - (g*t_no_ar**2)/2

  vfy = 2*(((yf-h_solo)/t_no_ar)-v0y/2)

  mod_final = math.sqrt(v0x**2+vfy**2)

  print("_______________________________")
  print("Velocidade prestes a atingir o chão:")
  print("Velocidade final x = %.3f"%v0x)
  print("Velocidade final y = %.3f"%vfy)
  print("Módulo = %.3f\n\n"%mod_final)
  
  input("Aperte enter para finalizar...")



#MENU
while(True):
  print(" __________________________________")
  print("|     Centro Universitário FEI     |")
  print("|__________________________________|")
  print("|______LANÇAMENTO DE PROJÉTIL______|")
  print("|__________________________________|")
  print("| Gabriel L. | Juan L. | Lorena C. |")
  print("|__________________________________|")
  input("|    Aperte enter para iniciar...  |\n")
  main()
