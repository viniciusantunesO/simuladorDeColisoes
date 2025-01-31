import pygame
import math
import random

# Inicializar o pygame
pygame.init()

# Configurações da janela
WIDTH = int(input('WIDTH:')) 
HEIGHT = int(input('HEIGHT:'))
NUM_BOLAS = int(input('numero de bolas:')) 
raio = int(input('raio:'))
janela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Colisões Elásticas 2D")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Classe para as bolas
class Ball:
    def __init__(self, x, y, raio, cor, vel):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.vx, self.vy = vel

    def mover(self):
        #Atualiza a posição das bolas
        self.x += self.vx
        self.y += self.vy

        # Verificar colisão com as bordas
        if self.x - self.raio < 0 or self.x + self.raio > WIDTH:
            self.vx = -self.vx
        if self.y - self.raio < 0 or self.y + self.raio > HEIGHT:
            self.vy = -self.vy

    def draw(self, janela):
        #Desenha as bolas na tela
        pygame.draw.circle(janela, self.cor, (int(self.x), int(self.y)), self.raio)

    def check_collision(self, other):
        # Distância entre os centros das bolas
        dx = other.x - self.x
        dy = other.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)

        if distancia < self.raio + other.raio:  # Colisão
            # Vetor unitário normal
            nx = dx / distancia
            ny = dy / distancia

            # Vetor tangente
            tx = -ny
            ty = nx

            # Decompor velocidades nos eixos normal e tangente
            v1n = self.vx * nx + self.vy * ny
            v1t = self.vx * tx + self.vy * ty
            v2n = other.vx * nx + other.vy * ny
            v2t = other.vx * tx + other.vy * ty

            # Trocar as velocidades normais (colisão elástica)
            v1n, v2n = v2n, v1n

            # Recombinar as velocidades
            self.vx = v1n * nx + v1t * tx
            self.vy = v1n * ny + v1t * ty
            other.vx = v2n * nx + v2t * tx
            other.vy = v2n * ny + v2t * ty

            # Reposicionar as bolas para evitar sobreposição
            overlap = 0.5 * (self.raio + other.raio - distancia + 1)
            self.x -= overlap * nx
            self.y -= overlap * ny
            other.x += overlap * nx
            other.y += overlap * ny

# Criar bolas dinamicamente
bolas = []
for _ in range(NUM_BOLAS):
    x = random.randint(raio, WIDTH - raio)
    y = random.randint(raio, HEIGHT - raio)
    vx = random.uniform(-5, 5)  # Velocidade aleatória no intervalo [-5, 5]
    vy = random.uniform(-5, 5)
    cor = random.choice([RED, BLUE])  # Cor aleatória entre vermelho e azul
    bolas.append(Ball(x, y, raio, cor, [vx, vy]))

# Loop principal
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        janela.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualizar posição e verificar colisões
        for ball in bolas:
            ball.mover()

        for i in range(len(bolas)):
            for j in range(i + 1, len(bolas)):
                bolas[i].check_collision(bolas[j])

        # Desenhar bolas
        for ball in bolas:
            ball.draw(janela)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()