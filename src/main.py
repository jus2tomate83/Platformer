from level import Level
from pytmx.util_pygame import load_pygame

from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
        pygame.display.set_caption('Pirate World')
        self.clock = pygame.time.Clock()
        self.import_assets()

        self.tmx_maps = {0: load_pygame( join('..','res','data','levels','omni.tmx') )}
        self.current_stage = Level(self.tmx_maps[0], self.level_frames)

    def import_assets(self):
        self.level_frames = {
            'flag' :import_folder('..','res','graphics','level','flag'),
            'saw' :import_folder('..','res','graphics','enemies','saw', 'animation'),
            'floor_spike': import_folder('..', 'res', 'graphics', 'enemies', 'floor_spikes'),
            'palms': import_sub_folders('..', 'res', 'graphics', 'level', 'palms'),
            'candle': import_folder('..', 'res', 'graphics', 'level', 'candle'),
            'window': import_folder('..', 'res', 'graphics', 'level', 'window'),
            'big_chain': import_folder('..', 'res', 'graphics', 'level', 'big_chain'),
            'small_chain': import_folder('..', 'res', 'graphics', 'level', 'small_chain'),
            'candle_light': import_folder('..', 'res', 'graphics', 'level', 'candle_light'),
            'player': import_sub_folders('..','res', 'graphics','player')
        }
        print("Player frame keys:", self.level_frames['palms'].keys())  # Debug print

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            print(self.clock.get_fps())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()