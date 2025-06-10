import pygame
import math
import random

# Inicializar o pygame
pygame.init()

# Função para entrada segura de inteiros
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite um número inteiro válido.")

# Configurações da janela e simulação
WIDTH = input_int('Largura da janela (WIDTH): ')
HEIGHT = input_int('Altura da janela (HEIGHT): ')
NUM_BOLAS = input_int('Número de bolas: ')
RAIO = input_int('Raio das bolas: ')

janela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Colisões Elásticas 2D")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Classe da bola
class Ball:
    def __init__(self, x, y, raio, cor, vel):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.vx, self.vy = vel

    def mover(self):
        self.x += self.vx
        self.y += self.vy

        # Corrigir posição se bater nas bordas
        if self.x - self.raio < 0:
            self.x = self.raio
            self.vx *= -1
        elif self.x + self.raio > WIDTH:
            self.x = WIDTH - self.raio
            self.vx *= -1

        if self.y - self.raio < 0:
            self.y = self.raio
            self.vy *= -1
        elif self.y + self.raio > HEIGHT:
            self.y = HEIGHT - self.raio
            self.vy *= -1


    def draw(self, surface):
        pygame.draw.circle(surface, self.cor, (int(self.x), int(self.y)), self.raio)

    def check_collision(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dist = math.hypot(dx, dy)

        if dist < self.raio + other.raio:
            # Vetor normal e tangente
            nx, ny = dx / dist, dy / dist
            tx, ty = -ny, nx

            # Decomposição das velocidades
            v1n = self.vx * nx + self.vy * ny
            v1t = self.vx * tx + self.vy * ty
            v2n = other.vx * nx + other.vy * ny
            v2t = other.vx * tx + other.vy * ty

            # Trocar componentes normais (elástica)
            v1n, v2n = v2n, v1n

            # Recombinação
            self.vx = v1n * nx + v1t * tx
            self.vy = v1n * ny + v1t * ty
            other.vx = v2n * nx + v2t * tx
            other.vy = v2n * ny + v2t * ty

            # Correção de sobreposição
            overlap = 0.5 * (self.raio + other.raio - dist + 1)
            self.x -= overlap * nx
            self.y -= overlap * ny
            other.x += overlap * nx
            other.y += overlap * ny

# Função para criar bolas sem sobreposição inicial
def criar_bolas():
    bolas = []
    tentativas_max = 5000

    for _ in range(NUM_BOLAS):
        for _ in range(tentativas_max):
            x = random.randint(RAIO, WIDTH - RAIO)
            y = random.randint(RAIO, HEIGHT - RAIO)
            nova_bola = Ball(x, y, RAIO, random.choice([RED, BLUE]), 
                             [random.uniform(-5, 5), random.uniform(-5, 5)])

            if all(math.hypot(x - b.x, y - b.y) > 2 * RAIO for b in bolas):
                bolas.append(nova_bola)
                break
        else:
            print("Não foi possível posicionar todas as bolas sem sobreposição.")
            break
    return bolas

# Função principal
def main():
    clock = pygame.time.Clock()
    bolas = criar_bolas()
    running = True

    while running:
        janela.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i, bola in enumerate(bolas):
            bola.mover()
            for j in range(i + 1, len(bolas)):
                bola.check_collision(bolas[j])
            bola.draw(janela)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()