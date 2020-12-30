import os

# 448,192,1117,1,4,0:0:0:0:
# The first value indicates which key the hit object is sent to
# The second indicates a static Y spawn(?)
# The third indicates at which frame of the song the note should be hit(?). If not the frame of hit, the frame of spawn.
# -> This will likely be relative to the `TimelineZoom` value in the .osu file's second section.
# The fourth indicates type of note.
# The sixth indicates time to hold (if note is hold)

# 1   = single tap
# 128 = hold

# 64  = D
# 192 = F
# 320 = J
# 448 = K


class Beatmap:

    def __init__(self, path, osu_file, audio, timeline_zoom=None):
        self._path = path
        self._audio = path + audio
        self._osu_file = path + osu_file
        self._timeline_zoom = timeline_zoom

        self.notes = {
            '64':  [],
            '192': [],
            '320': [],
            '448': []
        }

        with open(self._osu_file, 'r') as beatmap:
            timing_points = beatmap.read().split('[HitObjects]')[1]

            for point in timing_points.splitlines():
                parsed = self.parse_hit_object(point)
                if parsed != None:
                    self.notes[parsed.get('key')].append(parsed)

    def parse_hit_object(self, hit):
        _ = hit.split(',')
        hit_object = {}

        if len(_) < 2:
            return None

        hit_object['key'] = _[0]
        hit_object['spawn_frame'] = _[2]
        hit_object['note_type'] = _[3]
        hit_object['hold_duration'] = _[5].split(':')[0]
        return hit_object


