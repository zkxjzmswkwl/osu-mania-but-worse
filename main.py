import pygame
from settings import Settings

BEATMAP = [['d', 0], ['f', 150], ['j', 160], ['k', 180], ['d', 185], ['d', 195]]


class Note:

    def __init__(self, key, theme):
        self._key = key 
        self._theme = theme
        self.last_pos = None
        self.can_be_hit = True 

    def _draw(self, screen):
        pos_size = None

        if self.last_pos is None:
            if self._key == 'd':
                pos_size = [170, 680, 60, 30]
            elif self._key == 'f':
                pos_size = [290, 680, 60, 30]
            elif self._key == 'j':
                pos_size = [410, 680, 60, 30]
            elif self._key == 'k':
                pos_size = [530, 680, 60, 30]

            pygame.draw.rect(screen, self._theme.get(self._key), pygame.Rect(pos_size))
            self.last_pos = pos_size
        else:
            pygame.draw.rect(
                screen,
                self._theme.get(self._key),
                pygame.Rect(
                    self.last_pos[0],
                    self.last_pos[1] - 4,
                    self.last_pos[2],
                    self.last_pos[3]))
            self.last_pos[1] = self.last_pos[1] - 4


class Rhythm:

    def __init__(self, resolution=(1280, 720)):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.channel = pygame.mixer.find_channel(True)
        self.channel.set_volume(0.8)
        self._font = pygame.font.SysFont('Hack NF', 50)

        self._resolution = resolution
        self.__settings = Settings('settings.ini')
        self.__screen = pygame.display.set_mode(self._resolution)
        self.__clock = pygame.time.Clock()

        self.should_loop = True
        self.theme = self.__settings.get_theme()

        self.combo = 0
        self.notes = []
        self.rendered_notes = []

        self.hit_queue = []
        self.hit_sound = pygame.mixer.Sound('sounds/drum-hitnormal.wav')

        pygame.mixer.music.load('maps/blue_zenith/audio.ogg')
        pygame.mixer.music.play(-1)

    def send_hit(self, key):
        self.hit_queue.append(key)

    def input(self, e):
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            self.send_hit('d')
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_f:
            self.send_hit('f')
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_j:
            self.send_hit('j')
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_k:
            self.send_hit('k')

    def logic(self):
        for note in self.notes:
            if note.last_pos[1] in range(10, 80) and note.can_be_hit:
                for i, hit in enumerate(self.hit_queue):
                    if hit == note._key:
                        self.combo += 1
                        note.can_be_hit = False
                        self.channel.play(self.hit_sound)
                        self.hit_queue.pop(i)
                        print(self.hit_queue)

        # Parsing 'beatmap'
        for i, note in enumerate(BEATMAP):
            if i not in self.rendered_notes and note[1] <= 0:
                self.notes.append(Note(note[0], self.theme))
                self.rendered_notes.append(i)
            else:
                BEATMAP[i][1] -= 1

    def render(self):
        self.__screen.fill((0, 0, 0))
        for note in self.notes:
            note._draw(self.__screen)

        # Hit zones for each note
        pygame.draw.rect(self.__screen, (0, 200, 255), (160, 10, 80, 40), 3)
        pygame.draw.rect(self.__screen, (0, 200, 255), (280, 10, 80, 40), 3)
        pygame.draw.rect(self.__screen, (0, 200, 255), (400, 10, 80, 40), 3)
        pygame.draw.rect(self.__screen, (0, 200, 255), (520, 10, 80, 40), 3)

        combo_surface = self._font.render(str(self.combo), False, (255, 255, 255))
        self.__screen.blit(combo_surface, (20, 680))

        pygame.display.flip()

    def loop(self):
        key_down = pygame.key.get_pressed()

        while self.should_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.should_loop = False

                if event.type == pygame.KEYDOWN:
                    self.input(event)

            self.logic()
            self.render()
            self.__clock.tick(60)


if __name__ == '__main__':
    mania_clone = Rhythm()
    mania_clone.loop()
