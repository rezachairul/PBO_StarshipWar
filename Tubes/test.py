import sys
import random

import pygame
from pygame.locals import *

# Inisialisasi Pygame
pygame.init()

# Path file gambar player_ship
player_ship = 'D:/Reza/kuliah/pbo/Tubes/assets/img/player.png'  
enemy_ship = 'D:/Reza/kuliah/pbo/Tubes/assets/img/alien.png'
ufo_ship = 'D:/Reza/kuliah/pbo/Tubes/assets/img/alien2.png'
# Tentukan resolusi layar
s_width = 800  # Lebar layar
s_height = 600  # Tinggi layar
resolution = (s_width, s_height)  # Resolusi layar

# Buat jendela permainan
screen = pygame.display.set_mode(resolution)

# Toggle mode layar penuh
pygame.display.toggle_fullscreen()

# Inisialisasi clock untuk mengatur FPS
clock = pygame.time.Clock()
FPS = 60

background_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
ufo_group = pygame.sprite.Group()

sprite_group = pygame.sprite.Group()

# Kelas Background
class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((x, y))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        self.rect.x += 1
        if self.rect.y > s_height:
            self.rect.y = random.randrange(-10, 0)
            self.rect.x = random.randrange(-400, s_width)

# Kelas Player
class Player(pygame.sprite.Sprite):
    def __init__(self, img, scale_factor=0.5):
        super().__init__()
        original_image = pygame.image.load(img)
        self.image = pygame.transform.scale(original_image, (int(original_image.get_width() * scale_factor), int(original_image.get_height() * scale_factor)))
        self.rect = self.image.get_rect()  # Mengambil rect dari gambar player_ship
        self.image.set_colorkey((0, 0, 0))  # Set warna hitam sebagai transparansi

    def update(self):
        mouse = pygame.mouse.get_pos()
        self.rect.x = mouse[0]
        self.rect.y = mouse[1]

#Kelas Enemy
class Enemy(Player):
    def __init__(self, img, scale_factor=0.2):
        super().__init__(img, scale_factor)
        self.rect.x = random.randrange(0, s_width)
        self.rect.y = random.randrange(-500, 0)
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def update(self):
        self.rect.y += 1
        if self.rect.y > s_height:
             self.rect.y = random.randrange(-500, 0)  #Kembali ke atas layar dengan posisi random

class Ufo(Enemy):
    def __init__(self, img, scale_factor=0.2):
        super().__init__(img, scale_factor)
        self.rect.x = -200
        self.rect.y = 200
        self.move = 1

    def update(self):
        self.rect.x += self.move
        if self.rect.x > s_width + 200:
            self.move *= -1
        elif self.rect.x < -200:
            self.move *= -1


# Kelas Game
class Game:
    def __init__(self):
        self.run_game()

    def create_background(self):
        for i in range(25):
            x = random.randint(1, 5)
            background_image = Background(x, x)
            background_image.rect.x = random.randrange(0, s_width)
            background_image.rect.y = random.randrange(0, s_height)
            background_group.add(background_image)
            sprite_group.add(background_image)

    def create_player(self):
        self.player = Player(player_ship, scale_factor=0.2)
        player_group.add(self.player)
        sprite_group.add(self.player)

    def create_enemy(self):
        for i in range(10):
            self.enemy = Enemy(enemy_ship)
            enemy_group.add(self.enemy)
            sprite_group.add(self.enemy)

    def create_ufo(self):
        for i in range(3):
            self.ufo = Ufo(ufo_ship)
            ufo_group.add(self.ufo)
            sprite_group.add(self.ufo)

    def run_update(self):
        sprite_group.draw(screen)
        sprite_group.update()

    def run_game(self):
        self.create_background()
        self.create_player()
        self.create_enemy()
        self.create_ufo()
        while True:
            # Handle event
            screen.fill((0, 0, 0))
            self.run_update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            # Perbarui tampilan
            pygame.display.update()
            # Atur FPS
            clock.tick(FPS)

# Fungsi utama
def main():
    game = Game()

# Jalankan fungsi utama jika kode dijalankan sebagai program utama
if __name__ == '__main__':
    main()
