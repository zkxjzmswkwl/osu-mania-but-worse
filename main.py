import pygame
from settings import Settings
from beatmap import Beatmap
from note import Note
from lane import Lane


class Rhythm:

    def __init__(self, beatmap, resolution=(1280, 2000)):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.channel = pygame.mixer.find_channel(True)
        self.channel.set_volume(5.8)

        self.beatmap = beatmap
        self.resolution = resolution

        self._should_loop = True
        self._font = pygame.font.SysFont('Hack NF', 70)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(resolution)

        self._combo = 0

        self.d_lane = Lane(64)
        self.f_lane = Lane(192)
        self.j_lane = Lane(320)
        self.k_lane = Lane(448)

        self.populate_lanes()

        pygame.mixer.music.load(self.beatmap._audio)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

    def populate_lanes(self):
        for lane in self.beatmap.notes:
            if lane == '64':
                self.d_lane.load_objects(self.beatmap.notes.get(lane))
            elif lane == '192':
                self.f_lane.load_objects(self.beatmap.notes.get(lane))
            elif lane == '320':
                self.j_lane.load_objects(self.beatmap.notes.get(lane))
            elif lane == '448':
                self.k_lane.load_objects(self.beatmap.notes.get(lane))

    def input(self, event):
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            self.d_lane.send_hit()
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_f:
            self.f_lane.send_hit()
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_j:
            self.j_lane.send_hit()
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_k:
            self.k_lane.send_hit()

    def logic(self):
        pass

    def render(self):
        self._screen.fill((0, 0, 0))

        # Hit zones for each note
        pygame.draw.rect(self._screen, (0, 200, 255), (160, 10, 80, 40), 3)
        pygame.draw.rect(self._screen, (0, 200, 255), (280, 10, 80, 40), 3)
        pygame.draw.rect(self._screen, (0, 200, 255), (400, 10, 80, 40), 3)
        pygame.draw.rect(self._screen, (0, 200, 255), (520, 10, 80, 40), 3)

        combo_surface = self._font.render(str(self._combo), False, (255, 255, 255))

        self._screen.blit(combo_surface, (700, 10))

        pygame.display.flip()

    def loop(self):
        key_down = pygame.key.get_pressed()

        while self._should_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._should_loop = False

                if event.type == pygame.KEYDOWN:
                    self.input(event)

            self.logic()
            self.render()
            self._clock.tick(300)

titania= Beatmap('maps/titania/', 'titania_basic.osu', 'audio.ogg')
mania_clone = Rhythm(titania)
mania_clone.loop()
