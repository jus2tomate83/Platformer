from src.settings import *
from src.sprite.sprite import Sprite, MovingSprite
from src.player.player import Player
from src.groups.groups import AllSprites

class Level:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()

        #groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.sem_collision_sprite = pygame.sprite.Group()

        self.setup(tmx_map)

    def setup(self, tmx_map):
        #tiles
        for layer in ['BG', 'Terrain', 'FG', 'Platforms']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                groups = [self.all_sprites]
                if layer == 'Terrain': groups.append(self.collision_sprites)
                if layer == 'Platforms': groups.append(self.sem_collision_sprite)

                Sprite((x * TILED_SIZE, y * TILED_SIZE), surf, groups)

        #objects
        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                self.player = Player((obj.x, obj.y), (self.all_sprites,), self.collision_sprites, self.sem_collision_sprite)

        #moving object
        for obj in tmx_map.get_layer_by_name('Moving Objects'):
            if obj.name == 'helicopter':
                if obj.width > obj.height:
                    #horizontal
                    move_dir = 'x'
                    start_pos = (obj.x, obj.y + obj.height / 2)
                    end_pos = (obj.x + obj.width, obj.height / 2)
                else:
                    #vertical
                    move_dir = 'y'
                    start_pos = (obj.x + obj.width / 2, obj.y)
                    end_pos = (obj.x + obj.width / 2, obj.height)
                speed = obj.properties['speed']
                MovingSprite((self.all_sprites, self.sem_collision_sprite), start_pos, end_pos, move_dir, speed)

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.player.hitbox_rect.center)

