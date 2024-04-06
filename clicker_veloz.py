import pygame
import time 
from random import randint
pygame.init()

#creamos ventana
color_fondo = (200,255,255)
ventana = pygame.display.set_mode((500,500))
ventana.fill(color_fondo)
pygame.display.set_caption("Clicker Veloz")
clock = pygame.time.Clock()


#rectangulo

class Rectangulo():
    def __init__(self,x,y,ancho,alto,colorRectangulo):
        self.rect = pygame.Rect(x,y,ancho,alto)
        self.colorDeRelleno = colorRectangulo
    def cambiarColor(self,nuevoColor):
        self.colorDeRelleno = nuevoColor
    def rellenar(self):
        pygame.draw.rect(ventana, self.colorDeRelleno,self.rect)
    def bordear(self,colorBorde,anchoDelBorde):
        pygame.draw.rect(ventana,colorBorde,self.rect,anchoDelBorde)
    def estaClickeando(self,x,y):
        return self.rect.collidepoint(x,y)

class Etiqueta(Rectangulo):
    def cambiar_texto(self,texto,tamanioFuente,colorTexto):
        self.image = pygame.font.SysFont('verdana', tamanioFuente).render(texto, True, colorTexto)

    def dibujar(self,cambiarx,cambiary):
        self.rellenar()
        ventana.blit(self.image, (self.rect.x +cambiarx, self.rect.y + cambiary))        

AMARILLO = (255,255,0)
AZUL_OSCURO = (0,0,100)
AZUL = (80,80,255)
NEGRO = (0,0,0)
VERDE = (0,255,0)
ROJO = (255,0,0)
etiquetas = []

numero_tarjetas = 4

x = 70

for i in range (numero_tarjetas):
    nueva_etiqueta = Etiqueta(x,170,70,100,AMARILLO)
    nueva_etiqueta.bordear(AZUL,13)
    nueva_etiqueta.cambiar_texto("CLIC",20,NEGRO)
    etiquetas.append(nueva_etiqueta)
    x= x+100


esperar = 0 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            x,y = event.pos
            for i in range(0,numero_tarjetas):
                if etiquetas[i].estaClickeando(x,y):
                    if (i+1) == click:
                         etiquetas[i].cambiarColor(VERDE)
                    else:
                        etiquetas[i].cambiarColor(ROJO)
                    etiquetas[i].rellenar()
            
    if esperar == 0:
        esperar = 20
        click = randint(1,numero_tarjetas)
        for i in range(numero_tarjetas):
            etiquetas[i].cambiarColor(AMARILLO)
            if (i+1) == click:
                etiquetas[i].dibujar(10,35)
            else:
                 etiquetas[i].rellenar()
    else:
        esperar = esperar - 1

    

    pygame.display.update()
    clock.tick(40)