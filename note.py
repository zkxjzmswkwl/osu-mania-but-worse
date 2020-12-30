import pygame


class Note:

    def __init__(self, hit_object, theme):
        self._hit_object = hit_object
        self._theme = theme
        self._last_pos = None
        self._can_be_hit = True

        self._state = 'DEF'

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        return self._state

    def draw(self, screen):

        if self._hit_object == None:
            return

        pos_size = None

        if self.last_pos is None:
            if self._hit_object.get('key') == 64:
                pos_size = [170, 2000, 60, 30]
            elif self._hit_object.get('key') == 192:
                pos_size = [290, 2000, 60, 30]
            elif self._hit_object.get('key') == 320:
                pos_size = [410, 2000, 60, 30]
            elif self._hit_object.get('key') == 448:
                pos_size = [530, 2000, 60, 30]

            pygame.draw.rect(screen, self._theme.get(self._hit_object.get('key')), pygame.Rect(pos_size))
            self.last_pos = pos_size
        else:
            pygame.draw.rect(
                screen,
                self._theme.get(self._hit_object.get('key')),
                pygame.Rect(
                    self.last_pos[0],
                    self.last_pos[1] - 4,
                    self.last_pos[2],
                    self.last_pos[3]))
            self.last_pos[1] = self.last_pos[1] - 11
