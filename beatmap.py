import os


# 448,192,1117,1,4,0:0:0:0:
# 448,192 = keys (I think)
# Perhaps the numbers are their graphical offsets?
# If not, they're ids for the keys.
# 1117 is the ms in the song to place the hit objects at
# I don't know what 1 or 4 or 0:0:0:0: are yet.


class Beatmap:
    
    def __init__(self, path):
        self._path = path

    def read(self):
        with open(self._path, 'r') as beatmap:
            timing_points = beatmap.read().split('[HitObjects]')[1]
            timing_points = timing_points.splitlines()
            for a in timing_points:
                d = a.split(',')
                if len(d) < 2:
                    pass
                else:
                    print(f'Keys -> {d[3]}')
                    print(f'Timing -> {d[2]}')

    
   
a = Beatmap('maps/blue_zenith/blue_zenith.osu')
a.read()
