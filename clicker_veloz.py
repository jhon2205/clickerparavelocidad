import pygame
import time 
pygame.init()

#creamos ventana
color_fondo = (200,255,255)
ventana = pygame.display.set_mode((500,500))
ventana.fill(color_fondo)

clock = pygame.time.Clock()
pygame.display.set_caption("Clicker Veloz")
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
etiquetas = []

numero_tarjetas = 4

x = 70

for i in range (numero_tarjetas):
    nueva_etiqueta = Etiqueta(x,170,70,100,AMARILLO)
    nueva_etiqueta.bordear(AZUL,10)
    nueva_etiqueta.cambiar_texto("CLIC",26,NEGRO)
    etiquetas.append(nueva_etiqueta)
    x= x+100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    for eti in etiquetas:
        eti.dibujar(0,30)

    pygame.display.update()
    clock.tick(40)
