from src.settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        self.offset = vector()

    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - WINDOWS_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOWS_HEIGHT / 2)

        for sprites in sorted(self, key = lambda sprite: sprite.z):
            offset_pos = sprites.rect.topleft + self.offset
            self.display_surf.blit(sprites.image, offset_pos)