import pygame


class Lane:

    def __init__(self, key):
        self.key = key
        self._hit_objects = []


    def load_objects(self, objects):
        self._hit_objects = objects

    def get_objects(self):
        return self._hit_objects

    def send_hit(self):
        pass
